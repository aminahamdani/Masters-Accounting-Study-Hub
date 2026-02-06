"""
Application factory and initialization.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from database import get_engine, Base


def create_app() -> FastAPI:
    """
    Application factory function.
    Creates and configures the FastAPI application.
    """
    app = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION
    )
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_CREDENTIALS,
        allow_methods=settings.CORS_METHODS,
        allow_headers=settings.CORS_HEADERS,
    )
    
    # Register routers
    register_routers(app)
    
    # Register startup events
    register_startup_events(app)
    
    return app


def register_routers(app: FastAPI) -> None:
    """Register all application routers"""
    from routers import search, practice, progress, health
    
    app.include_router(health.router)
    app.include_router(search.router, prefix="/api")
    app.include_router(practice.router, prefix="/api")
    app.include_router(progress.router, prefix="/api")


def register_startup_events(app: FastAPI) -> None:
    """Register application startup events"""
    @app.on_event("startup")
    async def startup_event():
        """Initialize database tables on startup"""
        # Import models to ensure they're registered with Base.metadata
        from models import Topic, PracticeTemplate, ProgressLog  # noqa: F401
        
        try:
            engine = get_engine()
            if engine is not None:
                Base.metadata.create_all(bind=engine)
        except Exception as e:
            # Log the error but don't prevent server startup
            # Database endpoints will handle connection errors gracefully
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Could not initialize database on startup: {e}")
            logger.info("Server will continue to run. Database endpoints may not work until PostgreSQL is running.")
