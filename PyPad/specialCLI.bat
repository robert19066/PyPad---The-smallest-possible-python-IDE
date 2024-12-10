@echo off
setlocal enabledelayedexpansion
cls

rem Change the command prompt
set "PROMPT=(py-command mode) $P$G"

:cmdloop
set /p command="(PyPad special CLI mode) $pypad: "

if /i "!command!" == "run" (
    rem Call your Python script
    python script_to_run.py
) else if /i "!command!" == "runDebug" (
    rem Call your Python script with debug mode
    python script_to_run.py --debug
) else if /i "!command!" == "exitMode" (
    rem Switch back to the text editor mode (modify as needed)
    python editor.py
) else if /i "!command!" == "exitScript" (
    goto end
) else if /i "!command!" == "clear" (
    cls
) else if /i "!command!" == "help" (
    echo run - runs a Python script
    echo runDebug - runs a Python script in debug mode
    echo exitMode - switches to editor and vice versa
    echo exitScript - shuts down the whole app
    echo clear - clears the screen
    echo help - shows help information
    echo addLib - installs a Python package using pip
) else if /i "!command!" == "addLib" (
    set /p libname="Enter library name to install: "
    pip install !libname!
) else (
    echo Invalid command.
)
goto cmdloop

:end
endlocal
