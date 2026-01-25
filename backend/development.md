# Backend Development Setup

This guide will help you set up and run the Master's Accounting Study Hub backend locally.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Azure PostgreSQL database (or local PostgreSQL for development)
- Git (optional, for version control)

## Setup Instructions

### 1. Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Navigate to the backend directory and install the required packages:

```bash
cd backend
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the `backend` directory with your database credentials:

```env
# Azure PostgreSQL Connection Details
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_server.postgres.database.azure.com
DB_PORT=5432
DB_NAME=your_database_name

# Alternative: Use full connection string
# DATABASE_URL=postgresql://user:password@host:port/database
```

**Important:** Never commit the `.env` file to version control. Add it to `.gitignore`.

### 4. Run the Development Server

Start the FastAPI development server using Uvicorn:

```bash
# From the backend directory
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reload on code changes.

### 5. Test the API

Once the server is running, you can:

- Visit `http://localhost:8000` for the root endpoint
- Visit `http://localhost:8000/health` for the health check endpoint
- Visit `http://localhost:8000/docs` for the interactive API documentation (Swagger UI)
- Visit `http://localhost:8000/redoc` for alternative API documentation (ReDoc)

## Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── database.py          # SQLAlchemy database configuration
├── requirements.txt     # Python dependencies
├── development.md       # This file
├── .env                 # Environment variables (not in git)
├── routers/             # API route handlers
├── models/              # SQLAlchemy database models
└── schemas/             # Pydantic schemas for request/response validation
```

## Azure Deployment Notes

When deploying to Azure App Service:

1. Set environment variables in Azure Portal under Configuration > Application Settings
2. Ensure Azure PostgreSQL firewall allows connections from Azure App Service
3. Use managed identity or connection strings stored in Azure Key Vault for production
4. Configure CORS origins to match your frontend domain

## Troubleshooting

### Database Connection Issues

- Verify your `.env` file has correct credentials
- Check that Azure PostgreSQL firewall allows your IP address
- Ensure the database server is running and accessible

### Port Already in Use

If port 8000 is already in use, specify a different port:

```bash
uvicorn main:app --reload --port 8001
```

### Import Errors

Make sure you're running commands from the `backend` directory and your virtual environment is activated.
