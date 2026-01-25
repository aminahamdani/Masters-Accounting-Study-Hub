"""
Progress router for handling progress-related endpoints.
"""
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/progress",
    tags=["progress"]
)

@router.get("")
async def progress(
    db: Session = Depends(get_db)
):
    """
    Progress endpoint - to be implemented.
    
    Args:
        db: Database session dependency
        
    Returns:
        Progress data (to be implemented)
    """
    return {"message": "Progress functionality coming soon"}
