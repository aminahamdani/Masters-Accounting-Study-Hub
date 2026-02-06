"""
PracticeTemplate model for accounting practice scenarios.
"""
from sqlalchemy import Column, Integer, Text, ForeignKey, JSON
from database import Base


class PracticeTemplate(Base):
    """
    SQLAlchemy model for practice problem templates.
    
    Attributes:
        id: Primary key identifier
        topic_id: Foreign key to topics
        template_text: Scenario description / instructions
        expected_entries: JSON array of {account, debit, credit} for validation
    """
    __tablename__ = "practice_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    template_text = Column(Text, nullable=False)
    expected_entries = Column(JSON, nullable=True)  # [{account, debit, credit}, ...]
    
    def __repr__(self):
        return f"<PracticeTemplate(id={self.id}, topic_id={self.topic_id})>"
