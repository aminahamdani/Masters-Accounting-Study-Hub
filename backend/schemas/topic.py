"""
Pydantic schemas for Topic model.
"""
from pydantic import BaseModel
from typing import Optional


class TopicBase(BaseModel):
    """Base schema for Topic with common fields"""
    name: str
    oer_link: Optional[str] = None
    asc_reference: Optional[str] = None


class TopicCreate(TopicBase):
    """Schema for creating a new Topic"""
    pass


class TopicUpdate(BaseModel):
    """Schema for updating a Topic"""
    name: Optional[str] = None
    oer_link: Optional[str] = None
    asc_reference: Optional[str] = None


class Topic(TopicBase):
    """Schema for Topic response (includes id)"""
    id: int
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True
