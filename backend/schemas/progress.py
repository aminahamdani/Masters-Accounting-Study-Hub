"""
Pydantic schemas for progress tracking.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProgressLogCreate(BaseModel):
    """Create a progress log entry."""
    user_id: str
    topic_id: int
    status: str  # e.g. viewed, in_progress, mastered
    notes: Optional[str] = None


class ProgressLogOut(BaseModel):
    """Progress log response."""
    id: int
    user_id: str
    topic_id: int
    timestamp: datetime
    status: str
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class DashboardSummary(BaseModel):
    """Learning dashboard summary for a user."""
    user_id: str
    topics_viewed: int
    topics_in_progress: int
    topics_mastered: int
    recent_activity: list
