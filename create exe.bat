@echo off
setlocal

set "SCRIPT_NAME=youtube_downloader"

pip show pyinstaller >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] pyinstaller nicht gefunden. Installiere...
    pip install pyinstaller
)

echo [INFO] Erstelle EXE aus %SCRIPT_NAME%.py ...
pyinstaller --onefile "%SCRIPT_NAME%.py"


if exist dist\%SCRIPT_NAME%.exe (
    echo [ERFOLG] EXE wurde erstellt: dist\%SCRIPT_NAME%.exe
) else (
    echo [FEHLER] EXE konnte nicht erstellt werden.
)

endlocal
pause
