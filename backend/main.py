from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# Initialize FastAPI app
app = FastAPI(
    title="Master's Accounting Study Hub API",
    description="Backend API for Master's Accounting Study Hub",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "Master's Accounting Study Hub API"
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Master's Accounting Study Hub API",
        "version": "1.0.0"
    }
