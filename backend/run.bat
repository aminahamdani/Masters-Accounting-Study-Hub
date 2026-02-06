@echo off
REM Run the Study Hub (backend serves frontend at http://127.0.0.1:8000/app/)
cd /d "%~dp0"
echo Installing dependencies if needed...
pip install -q -r requirements.txt 2>nul
echo.
echo Starting server. Open in browser: http://127.0.0.1:8000/
echo (You will be redirected to http://127.0.0.1:8000/app/)
echo Press Ctrl+C to stop.
echo.
uvicorn main:app --reload --host 127.0.0.1 --port 8000
