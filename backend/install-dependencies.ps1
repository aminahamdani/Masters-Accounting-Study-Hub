# PowerShell script to install dependencies in .venv
# Run this script from the backend directory

Write-Host "Installing dependencies in virtual environment..." -ForegroundColor Green

# Check if .venv exists
if (Test-Path .venv\Scripts\python.exe) {
    Write-Host "Using existing virtual environment..." -ForegroundColor Yellow
    $pythonPath = ".venv\Scripts\python.exe"
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    $pythonPath = ".venv\Scripts\python.exe"
}

# Install dependencies using python -m pip
Write-Host "Installing packages from requirements.txt..." -ForegroundColor Green
& $pythonPath -m pip install --upgrade pip
& $pythonPath -m pip install -r requirements.txt

# Verify installations
Write-Host ""
Write-Host "Verifying installations..." -ForegroundColor Green
$packages = @(
    @{Name="fastapi"; Check="fastapi"},
    @{Name="uvicorn"; Check="uvicorn"},
    @{Name="sqlalchemy"; Check="sqlalchemy"},
    @{Name="psycopg2-binary"; Check="psycopg2"},
    @{Name="python-dotenv"; Check="dotenv"}
)

foreach ($package in $packages) {
    $result = & $pythonPath -m pip show $package.Check 2>$null
    if ($result) {
        Write-Host "OK $($package.Name) is installed" -ForegroundColor Green
    } else {
        Write-Host "FAIL $($package.Name) is NOT installed" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "To activate the virtual environment, run:" -ForegroundColor Cyan
Write-Host ".venv\Scripts\Activate.ps1" -ForegroundColor Cyan
