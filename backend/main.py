"""
Main application entry point.
Uses modular architecture with separated concerns.
"""
from fastapi import FastAPI
from core.app import create_app
from config import settings

# Create application instance using factory pattern
app: FastAPI = create_app()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Master's Accounting Study Hub API",
        "version": settings.API_VERSION
    }
