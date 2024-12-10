#!/bin/bash
clear
# Change the command prompt
PS1="(py-command mode) \w$ "

while true; do
    read -p "(PyPad special CLI mode) pypadCLI:   " command

    case $command in
        run)
            # Call your Python script
            python3 script_to_run.py
            ;;
        runDebug)
            # Call your Python script with debug mode
            python3 script_to_run.py --debug
            ;;
        exitMode)
            # Switch back to the text editor mode (modify as needed)
            ./editor.sh
            ;;
        exitScript)
            break
            ;;
        clear)
            clear
            ;;
        *)
            echo "Invalid command."
            ;;
    esac
done
