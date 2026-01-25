"""
Topic model for accounting study topics.
"""
from sqlalchemy import Column, Integer, String
from database import Base


class Topic(Base):
    """
    SQLAlchemy model for accounting study topics.
    
    Attributes:
        id: Primary key identifier
        name: Topic name (required)
        oer_link: Open Educational Resource link (optional)
        asc_reference: ASC (Accounting Standards Codification) reference (optional)
    """
    __tablename__ = "topics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    oer_link = Column(String, nullable=True)
    asc_reference = Column(String, nullable=True)
    
    def __repr__(self):
        return f"<Topic(id={self.id}, name='{self.name}')>"
