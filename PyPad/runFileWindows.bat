@echo off
setlocal enabledelayedexpansion

rem Read the filename from file_to_run.txt
set file_to_run=
for /f "usebackq delims=" %%i in ("fileToBeRunName.txt") do set file_to_run=%%i

rem Run the Python script
python !file_to_run!
pause
