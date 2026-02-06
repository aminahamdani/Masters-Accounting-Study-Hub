"""
Database configuration and session management for Azure PostgreSQL.
Uses SQLAlchemy with psycopg2-binary driver.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings
from typing import Optional

# Lazy initialization - engine created only when needed
_engine: Optional[object] = None
_SessionLocal: Optional[sessionmaker] = None

def get_engine():
    """Get or create the database engine (lazy initialization)"""
    global _engine, engine
    if _engine is None:
        try:
            # Get database URL from settings (synchronous driver)
            DATABASE_URL = settings.get_database_url(async_driver=False)
            # Create SQLAlchemy engine for Azure PostgreSQL
            _engine = create_engine(
                DATABASE_URL,
                pool_pre_ping=True,
                pool_size=settings.DB_POOL_SIZE,
                max_overflow=settings.DB_MAX_OVERFLOW,
                echo=settings.DB_ECHO
            )
            engine = _engine
        except (ValueError, Exception):
            # Missing config or connection error: allow app to run without DB
            _engine = None
            engine = None
            return None
    return _engine

def get_session_local():
    """Get or create the session maker (lazy initialization)"""
    global _SessionLocal
    if _SessionLocal is None:
        engine = get_engine()
        if engine is None:
            return None
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return _SessionLocal

# Create Base class for models
Base = declarative_base()

# For backward compatibility - direct access to engine
# This will be None until get_engine() is called
engine = None

# Dependency to get database session
def get_db():
    """
    Dependency function to get database session.
    Use this in FastAPI route dependencies.
    
    Yields:
        Session: Database session that will be automatically closed
        
    Raises:
        ValueError: If database configuration is missing
    """
    SessionLocal = get_session_local()
    if SessionLocal is None:
        raise ValueError(
            "Database not configured. Please set database credentials in .env file. "
            "See .env.example for required variables."
        )
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
