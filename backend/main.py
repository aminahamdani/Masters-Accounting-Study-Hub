"""
Main application entry point.
Uses modular architecture with separated concerns.
Serves the frontend from this same server so one URL works (no CORS).
"""
from pathlib import Path
from fastapi.responses import RedirectResponse
from core.app import create_app
from config import settings

# Create application instance using factory pattern
app = create_app()

# Serve frontend at /app so API routes (/health, /api) are not overridden
_frontend = Path(__file__).resolve().parent.parent / "frontend"
if _frontend.exists():
    from fastapi.staticfiles import StaticFiles
    app.mount("/app", StaticFiles(directory=str(_frontend), html=True), name="frontend")
    @app.get("/")
    async def root():
        return RedirectResponse(url="/app/", status_code=302)
else:
    @app.get("/")
    async def root():
        return {"message": "Welcome to Master's Accounting Study Hub API", "version": settings.API_VERSION}
