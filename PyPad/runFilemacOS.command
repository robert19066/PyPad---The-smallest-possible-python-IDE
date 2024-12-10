#!/bin/bash
chmod +x runFilemacOS.command


# Read the filename from file_to_run.txt
file_to_run=$(cat file_to_run.txt)

# Run the Python script
python3 "$file_to_run"

