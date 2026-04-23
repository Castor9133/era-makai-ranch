@echo off
chcp 65001 >nul
set "SRC=C:\Users\范振宁\Downloads\era\ERB\○TRAIN\COMMAND"
set "DST=%~dp0..\ERB\○TRAIN\COMMAND"
if not exist "%SRC%" (
  echo [ERROR] Vanilla COMMAND folder not found:
  echo   %SRC%
  echo Edit SRC in this .cmd to your install path, then run again.
  exit /b 1
)
if not exist "%DST%" mkdir "%DST%"
rem Copy all; do not overwrite the modded props file in DST (exclude from copy source side)
rem Robocopy /XF excludes matching filenames from the copy set from source
robocopy "%SRC%" "%DST%" /E /NFL /NDL /NJH /NJS /R:1 /W:1 /XF "COM200-299_道具.ERB"
if %ERRORLEVEL% GEQ 8 exit /b 1
echo.
echo OK: merged vanilla COMMAND into:
echo   %DST%
echo Preserved: COM200-299_道具.ERB (if present in destination; not overwritten from vanilla)
exit /b 0
