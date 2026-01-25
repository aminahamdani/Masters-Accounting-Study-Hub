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

Navigate to the backend directory and install the required packages.

**For Windows (PowerShell or Command Prompt):**

If you have a virtual environment in `.venv`, use one of these methods:

**Option 1: Using the installation script (Recommended)**
```powershell
cd backend
.\install-dependencies.ps1
```

Or if PowerShell scripts are blocked, use the batch file:
```cmd
cd backend
install-dependencies.bat
```

**Option 2: Manual installation**
```powershell
# Activate the virtual environment first
.venv\Scripts\Activate.ps1

# Then install dependencies
python -m pip install -r requirements.txt
```

**Option 3: Direct path to pip in .venv**
```powershell
cd backend
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Note:** If you get a "pip is not recognized" error, use `python -m pip` instead of just `pip`.

### 3. Environment Variables

Create a `.env` file in the `backend` directory with your database credentials. You can copy `.env.example` to `.env` as a starting point:

```bash
cp .env.example .env
```

Then edit `.env` with your actual Azure PostgreSQL credentials:

```env
# Azure PostgreSQL Connection Details
DB_HOST=your-db-host.postgres.database.azure.com
DB_PORT=5432
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_NAME=your-db-name

# Alternative: Use full connection string (for async driver)
# DATABASE_URL=postgresql+asyncpg://user:password@host:port/database
```

**Important:** Never commit the `.env` file to version control. It's already in `.gitignore`.

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
├── config.py            # Application configuration
├── database.py          # Async SQLAlchemy database configuration
├── requirements.txt     # Python dependencies
├── development.md       # This file
├── .env.example         # Environment variables template (safe to commit)
├── .env                 # Environment variables (not in git)
├── core/                # Core application components
│   └── app.py           # Application factory
├── routers/             # API route handlers
│   ├── health.py        # Health check router
│   ├── search.py        # Search router
│   ├── practice.py      # Practice router
│   └── progress.py      # Progress router
├── models/             # SQLAlchemy database models
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
