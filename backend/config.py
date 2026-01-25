"""
Configuration module for the application.
Centralizes all configuration settings.
"""
import os
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    # API Settings
    API_TITLE: str = "Master's Accounting Study Hub API"
    API_DESCRIPTION: str = "Backend API for Master's Accounting Study Hub"
    API_VERSION: str = "1.0.0"
    
    # CORS Settings
    CORS_ORIGINS: List[str] = os.getenv(
        "CORS_ORIGINS", 
        "*"
    ).split(",") if os.getenv("CORS_ORIGINS") != "*" else ["*"]
    CORS_CREDENTIALS: bool = os.getenv("CORS_CREDENTIALS", "true").lower() == "true"
    CORS_METHODS: List[str] = os.getenv("CORS_METHODS", "*").split(",") if os.getenv("CORS_METHODS") != "*" else ["*"]
    CORS_HEADERS: List[str] = os.getenv("CORS_HEADERS", "*").split(",") if os.getenv("CORS_HEADERS") != "*" else ["*"]
    
    # Database Settings
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Database Pool Settings
    DB_POOL_SIZE: int = int(os.getenv("DB_POOL_SIZE", "5"))
    DB_MAX_OVERFLOW: int = int(os.getenv("DB_MAX_OVERFLOW", "10"))
    DB_ECHO: bool = os.getenv("DB_ECHO", "false").lower() == "true"
    
    @classmethod
    def get_database_url(cls, async_driver: bool = True) -> str:
        """
        Construct database URL from environment variables.
        
        Args:
            async_driver: If True, returns URL with asyncpg driver (postgresql+asyncpg://)
                        If False, returns standard PostgreSQL URL (postgresql://)
        
        Returns:
            Database connection URL string
        """
        if cls.DATABASE_URL:
            # If DATABASE_URL is provided, ensure it uses async driver if needed
            if async_driver and cls.DATABASE_URL.startswith("postgresql://"):
                return cls.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
            return cls.DATABASE_URL
        
        if not all([cls.DB_USER, cls.DB_PASSWORD, cls.DB_HOST, cls.DB_NAME]):
            raise ValueError(
                "Database configuration missing. Please set either DATABASE_URL or "
                "all of: DB_USER, DB_PASSWORD, DB_HOST, DB_NAME"
            )
        
        protocol = "postgresql+asyncpg" if async_driver else "postgresql"
        return f"{protocol}://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"

# Global settings instance
settings = Settings()
