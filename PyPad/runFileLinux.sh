#!/bin/bash

# Read the filename from file_to_run.txt
file_to_run=$(cat fileToBeRunName.txt)

# Run the Python script
python3 "$file_to_run"
