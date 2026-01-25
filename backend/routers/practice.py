"""
Practice router for handling practice-related endpoints.
"""
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/practice",
    tags=["practice"]
)

@router.get("")
async def practice(
    db: Session = Depends(get_db)
):
    """
    Practice endpoint - to be implemented.
    
    Args:
        db: Database session dependency
        
    Returns:
        Practice data (to be implemented)
    """
    return {"message": "Practice functionality coming soon"}
