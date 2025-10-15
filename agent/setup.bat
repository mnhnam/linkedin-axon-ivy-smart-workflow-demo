@echo off
setlocal

echo Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install Python dependencies.
    exit /b %errorlevel%
)

echo Installing Playwright browser (Chromium) with dependencies...
playwright install chromium --with-deps
if %errorlevel% neq 0 (
    echo Failed to install Playwright Chromium.
    exit /b %errorlevel%
)

echo Setup complete. You can now run the web crawler!
echo.
endlocal
pause
