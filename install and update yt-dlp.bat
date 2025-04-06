@echo off
setlocal

where yt-dlp >nul 2>&1

if %ERRORLEVEL%==0 (
    echo yt-dlp ist bereits installiert. Aktualisiere...
    yt-dlp -U
) else (
    echo yt-dlp ist nicht installiert. Installiere...
    curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -o yt-dlp.exe
    if exist yt-dlp.exe (
        echo yt-dlp wurde erfolgreich heruntergeladen.
        yt-dlp -U
    ) else (
        echo Fehler beim Herunterladen von yt-dlp.
    )
)

endlocal
pause