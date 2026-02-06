"""
Practice router: practice templates and Ledger Simulator validation.
"""
from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from database import get_db
from sqlalchemy.orm import Session
from models.topic import Topic
from models.practice_template import PracticeTemplate
from schemas.practice import (
    PracticeTemplateOut,
    LedgerValidateRequest,
    LedgerValidateResponse,
    JournalEntryLine,
)

router = APIRouter(
    prefix="/practice",
    tags=["practice"],
)


@router.get("", response_model=List[PracticeTemplateOut])
async def list_practice_templates(
    topic_id: Optional[int] = Query(None, description="Filter by topic ID"),
    db: Session = Depends(get_db),
):
    """
    List practice templates, optionally filtered by topic.
    Excludes expected_entries in list view (use GET /practice/{id} for full template).
    """
    q = db.query(PracticeTemplate)
    if topic_id is not None:
        q = q.filter(PracticeTemplate.topic_id == topic_id)
    templates = q.order_by(PracticeTemplate.id).all()
    return [
        PracticeTemplateOut(
            id=t.id,
            topic_id=t.topic_id,
            template_text=t.template_text,
            expected_entries=None,
        )
        for t in templates
    ]


@router.get("/topics", response_model=List[dict])
async def list_topics_for_practice(db: Session = Depends(get_db)):
    """List all topics that have at least one practice template (id, name)."""
    from sqlalchemy import func
    rows = (
        db.query(Topic.id, Topic.name)
        .join(PracticeTemplate, PracticeTemplate.topic_id == Topic.id)
        .distinct()
        .all()
    )
    return [{"id": r.id, "name": r.name} for r in rows]


@router.get("/{template_id}", response_model=PracticeTemplateOut)
async def get_practice_template(
    template_id: int,
    db: Session = Depends(get_db),
):
    """Get a single practice template including expected_entries for Ledger Simulator."""
    t = db.query(PracticeTemplate).filter(PracticeTemplate.id == template_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Practice template not found")
    return PracticeTemplateOut(
        id=t.id,
        topic_id=t.topic_id,
        template_text=t.template_text,
        expected_entries=t.expected_entries,
    )


def _normalize_entries(entries: List[JournalEntryLine]) -> List[dict]:
    """Normalize to comparable dicts: account stripped/lower, debit/credit as float."""
    out = []
    for e in entries:
        out.append({
            "account": (e.account or "").strip().lower(),
            "debit": round(float(e.debit or 0), 2),
            "credit": round(float(e.credit or 0), 2),
        })
    return out


def _entries_balance(entries: List[dict]) -> tuple[bool, float, float]:
    total_d = sum(x["debit"] for x in entries)
    total_c = sum(x["credit"] for x in entries)
    return (abs(total_d - total_c) < 0.01, round(total_d, 2), round(total_c, 2))


@router.post("/ledger/validate", response_model=LedgerValidateResponse)
async def validate_ledger(
    body: LedgerValidateRequest,
    template_id: Optional[int] = Query(None, description="If provided, check against this practice template"),
    db: Session = Depends(get_db),
):
    """
    Ledger Simulator: validate that debits equal credits.
    If template_id is provided, also check that entries match the expected solution.
    """
    if not body.entries:
        return LedgerValidateResponse(
            balanced=False,
            total_debits=0,
            total_credits=0,
            message="No entries provided.",
            hint="Add at least one debit and one credit line.",
        )
    entries = _normalize_entries(body.entries)
    balanced, total_d, total_c = _entries_balance(entries)
    if not balanced:
        return LedgerValidateResponse(
            balanced=False,
            total_debits=total_d,
            total_credits=total_c,
            message="Entries do not balance. Debits must equal credits.",
            hint="Total debits and total credits must be equal.",
        )
    if template_id is None:
        return LedgerValidateResponse(
            balanced=True,
            total_debits=total_d,
            total_credits=total_c,
            message="Entries balance. Debits equal credits.",
        )
    t = db.query(PracticeTemplate).filter(PracticeTemplate.id == template_id).first()
    if not t or not t.expected_entries:
        return LedgerValidateResponse(
            balanced=True,
            total_debits=total_d,
            total_credits=total_c,
            message="Entries balance. (No solution to compare against.)",
        )
    expected = _normalize_entries(
        [JournalEntryLine(account=e.get("account", ""), debit=float(e.get("debit", 0) or 0), credit=float(e.get("credit", 0) or 0)) for e in t.expected_entries]
    )
    # Sort both by account and amounts for comparison
    def key(x):
        return (x["account"], x["debit"], x["credit"])
    expected_sorted = sorted(expected, key=key)
    actual_sorted = sorted(entries, key=key)
    correct = expected_sorted == actual_sorted
    return LedgerValidateResponse(
        balanced=True,
        total_debits=total_d,
        total_credits=total_c,
        correct=correct,
        message="Entries balance. " + ("Your solution matches the expected solution." if correct else "Your solution does not match the expected solution. Check accounts and amounts."),
        hint=None if correct else "Compare each line: account name and debit/credit amounts.",
    )
