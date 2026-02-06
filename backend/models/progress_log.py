"""
ProgressLog model for user study progress.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, text
from database import Base


class ProgressLog(Base):
    """
    SQLAlchemy model for progress logs.
    
    Attributes:
        id: Primary key
        user_id: User identifier
        topic_id: Foreign key to topics
        timestamp: When the progress was recorded
        status: viewed, in_progress, mastered
        notes: Optional notes
    """
    __tablename__ = "progress_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    status = Column(String(50), nullable=False, index=True)
    notes = Column(Text, nullable=True)
