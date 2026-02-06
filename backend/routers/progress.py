"""
Progress router: log and retrieve study progress for the learning dashboard.
"""
from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.progress_log import ProgressLog
from models.topic import Topic
from schemas.progress import ProgressLogCreate, ProgressLogOut, DashboardSummary

router = APIRouter(
    prefix="/progress",
    tags=["progress"],
)


@router.post("", response_model=ProgressLogOut)
async def log_progress(body: ProgressLogCreate, db: Session = Depends(get_db)):
    """Log progress for a user/topic (viewed, in_progress, mastered)."""
    log = ProgressLog(
        user_id=body.user_id,
        topic_id=body.topic_id,
        status=body.status,
        notes=body.notes,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


@router.get("", response_model=List[ProgressLogOut])
async def get_progress(
    user_id: str = Query(..., description="User identifier"),
    topic_id: Optional[int] = Query(None),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    """Get progress logs for a user, optionally filtered by topic."""
    q = db.query(ProgressLog).filter(ProgressLog.user_id == user_id)
    if topic_id is not None:
        q = q.filter(ProgressLog.topic_id == topic_id)
    logs = q.order_by(desc(ProgressLog.timestamp)).limit(limit).all()
    return logs


@router.get("/dashboard", response_model=DashboardSummary)
async def get_dashboard(
    user_id: str = Query(..., description="User identifier"),
    db: Session = Depends(get_db),
):
    """
    Personalized learning dashboard: counts of viewed, in progress, mastered,
    and recent activity.
    """
    # Most recent status per topic (order by timestamp desc, first occurrence wins)
    topic_status = {}
    for row in db.query(ProgressLog).filter(ProgressLog.user_id == user_id).order_by(desc(ProgressLog.timestamp)).all():
        if row.topic_id not in topic_status:
            topic_status[row.topic_id] = row.status
    viewed = sum(1 for s in topic_status.values() if s == "viewed")
    in_progress = sum(1 for s in topic_status.values() if s == "in_progress")
    mastered = sum(1 for s in topic_status.values() if s == "mastered")
    # Recent activity: last 10 logs with topic names
    recent = (
        db.query(ProgressLog, Topic.name)
        .join(Topic, Topic.id == ProgressLog.topic_id)
        .filter(ProgressLog.user_id == user_id)
        .order_by(desc(ProgressLog.timestamp))
        .limit(10)
        .all()
    )
    recent_activity = [
        {"topic_id": r[0].topic_id, "topic_name": r[1], "status": r[0].status, "timestamp": r[0].timestamp.isoformat() if r[0].timestamp else None}
        for r in recent
    ]
    return DashboardSummary(
        user_id=user_id,
        topics_viewed=viewed,
        topics_in_progress=in_progress,
        topics_mastered=mastered,
        recent_activity=recent_activity,
    )
