@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if errorlevel 1 (
  echo Python launcher not found. Install Python 3.12 x64 and enable PATH first.
  pause
  exit /b 1
)

where ffmpeg >nul 2>nul
if errorlevel 1 (
  echo FFmpeg not found. Install FFmpeg and add its bin folder to PATH first.
  pause
  exit /b 1
)

where ffprobe >nul 2>nul
if errorlevel 1 (
  echo ffprobe not found. Install the full FFmpeg Windows build and add its bin folder to PATH.
  pause
  exit /b 1
)

py -3.12 -m venv .venv
if errorlevel 1 goto failed
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if errorlevel 1 goto failed
pip install -r requirements.txt
if errorlevel 1 goto failed

python generate_starter_audio.py
if errorlevel 1 goto failed

if not exist .env copy .env.example .env >nul
echo.
echo Setup complete. Edit .env and add your own ElevenLabs/CIT settings.
pause
exit /b 0

:failed
echo.
echo Setup failed. Read HUONG_DAN_SETUP.md and check Python/FFmpeg installation.
pause
exit /b 1
