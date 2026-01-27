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

### 3. Database Setup

#### Option A: Local PostgreSQL Database

**Step 1: Create a local PostgreSQL database**

```bash
# Using psql command line
psql -U postgres
CREATE DATABASE studyhub;
\q
```

**Step 2: Run schema.sql to create tables**

You can use either the infrastructure folder schema or the backend schema:

```bash
# Using infrastructure schema (recommended)
psql -U postgres -d studyhub -f infrastructure/schema.sql

# Or using backend schema
psql -U postgres -d studyhub -f backend/schema.sql

# Or using the migration file
psql -U postgres -d studyhub -f backend/migrations/001_initial_schema.sql
```

**Step 3: Run seed_data.sql to populate topics**

```bash
# Using infrastructure seed data (recommended)
psql -U postgres -d studyhub -f infrastructure/seed_data.sql

# Or using backend seed data
psql -U postgres -d studyhub -f backend/seed_data.sql
```

**Step 4: Set environment variables using .env**

Create a `.env` file in the `backend` directory:

```bash
# Windows
Copy-Item .env.example .env

# macOS/Linux
cp .env.example .env
```

Then edit `.env` with your local database credentials:

```env
# Local PostgreSQL Connection Details
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your-local-password
DB_NAME=studyhub
```

#### Option B: Azure PostgreSQL Database

Create a `.env` file in the `backend` directory with your Azure PostgreSQL credentials. You can copy `.env.example` to `.env` as a starting point:

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
```

**Important:** Never commit the `.env` file to version control. It's already in `.gitignore`.

### 4. Run the Development Server

Start the FastAPI development server using Uvicorn:

```bash
# From the backend directory
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or if your virtual environment is activated:

```bash
uvicorn main:app --reload
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
├── database.py          # SQLAlchemy database configuration
├── requirements.txt     # Python dependencies
├── development.md       # This file
├── setup_database.md    # Database setup instructions
├── .env.example         # Environment variables template (safe to commit)
├── .env                 # Environment variables (not in git)
├── schema.sql           # Database schema (legacy)
├── seed_data.sql        # Seed data (legacy)
├── install-dependencies.ps1  # Windows PowerShell installation script
├── install-dependencies.bat  # Windows Batch installation script
├── core/                # Core application components
│   └── app.py           # Application factory
├── routers/             # API route handlers
│   ├── health.py        # Health check router
│   ├── search.py        # Search router
│   ├── practice.py      # Practice router
│   └── progress.py      # Progress router
├── models/              # SQLAlchemy database models
│   └── topic.py         # Topic model
├── schemas/             # Pydantic schemas for request/response validation
│   └── topic.py         # Topic schemas
└── migrations/          # Database migration files
    └── 001_initial_schema.sql
```

**Note:** The `infrastructure/` folder at the project root contains the canonical database schema and seed data files.

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

### Server Starts But Database Connection Fails

The server is designed to start even if PostgreSQL is not running. Database endpoints will return errors until PostgreSQL is available. To fix:

1. Ensure PostgreSQL is running on your system
2. Verify your `.env` file has the correct database credentials
3. Check that the database `studyhub` exists
4. Restart the FastAPI server

### Windows PowerShell Execution Policy

If you encounter execution policy errors when running `.ps1` scripts:

```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Or use the `.bat` file instead:
```cmd
install-dependencies.bat
```
