"""
Pydantic schemas for PracticeTemplate and Ledger Simulator.
"""
from pydantic import BaseModel
from typing import Optional, List, Any


class JournalEntryLine(BaseModel):
    """Single line in a journal entry (debit or credit)."""
    account: str
    debit: float = 0
    credit: float = 0


class PracticeTemplateOut(BaseModel):
    """Practice template response (for listing)."""
    id: int
    topic_id: int
    template_text: str
    expected_entries: Optional[List[Any]] = None

    class Config:
        from_attributes = True


class LedgerValidateRequest(BaseModel):
    """Request body for Ledger Simulator validation."""
    entries: List[JournalEntryLine]


class LedgerValidateResponse(BaseModel):
    """Response from Ledger Simulator validation."""
    balanced: bool
    total_debits: float
    total_credits: float
    hint: Optional[str] = None
    correct: Optional[bool] = None  # When validating against a scenario
    message: str
