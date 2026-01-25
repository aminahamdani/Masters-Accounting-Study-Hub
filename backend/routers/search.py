"""
Search router for handling search-related endpoints.
"""
from fastapi import APIRouter, Depends, Query
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models.topic import Topic
from schemas.topic import Topic as TopicSchema

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

@router.get("", response_model=List[TopicSchema])
async def search(
    q: str = Query(..., description="Search query string"),
    db: Session = Depends(get_db)
):
    """
    Search topics by name (case-insensitive).
    
    Args:
        q: Search query string
        db: Database session dependency
        
    Returns:
        List of topics matching the search query
    """
    # Query Topic table where name ILIKE %q%
    topics = db.query(Topic).filter(
        Topic.name.ilike(f"%{q}%")
    ).all()
    
    return topics
