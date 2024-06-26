@echo off

set "SCRIPT_VERSION=1.0.1"

REM Check if the user provided the -v or --version option
if "%1" == "-v" (
    echo pygame_generator version %SCRIPT_VERSION%
    exit /b
)
if "%1" == "--version" (
    echo pygame_generator version %SCRIPT_VERSION%
    exit /b
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not found in PATH
    pause
    exit /b
)

REM Set the directory of the Python script
set "SCRIPT_PATH=%~dp0pygame_generator.py"

REM Run the Python script
python "%SCRIPT_PATH%"
