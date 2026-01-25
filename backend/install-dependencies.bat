@echo off
REM Batch script to install dependencies in .venv
REM Run this script from the backend directory

echo Installing dependencies in virtual environment...

REM Check if .venv exists
if exist .venv\Scripts\python.exe (
    echo Using existing virtual environment...
    set PYTHON_PATH=.venv\Scripts\python.exe
) else (
    echo Creating virtual environment...
    python -m venv .venv
    set PYTHON_PATH=.venv\Scripts\python.exe
)

REM Install dependencies
echo Installing packages from requirements.txt...
%PYTHON_PATH% -m pip install --upgrade pip
%PYTHON_PATH% -m pip install -r requirements.txt

REM Verify installations
echo.
echo Verifying installations...
%PYTHON_PATH% -m pip show fastapi >nul 2>&1 && echo [OK] fastapi || echo [FAIL] fastapi
%PYTHON_PATH% -m pip show uvicorn >nul 2>&1 && echo [OK] uvicorn || echo [FAIL] uvicorn
%PYTHON_PATH% -m pip show sqlalchemy >nul 2>&1 && echo [OK] sqlalchemy || echo [FAIL] sqlalchemy
%PYTHON_PATH% -m pip show psycopg2-binary >nul 2>&1 && echo [OK] psycopg2-binary || echo [FAIL] psycopg2-binary
%PYTHON_PATH% -m pip show python-dotenv >nul 2>&1 && echo [OK] python-dotenv || echo [FAIL] python-dotenv

echo.
echo Installation complete!
echo To activate the virtual environment, run:
echo   .venv\Scripts\activate.bat
pause
