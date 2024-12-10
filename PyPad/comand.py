import subprocess
import os

def redirect():
    if os.name == 'nt':  # For Windows
        subprocess.run(['specialCLI.bat'], shell=True, check=True)
        subprocess.run(['./' + 'specialCLI.sh'], shell=True, check=True)

if __name__ == "__main__":
    print("if you see this is not ok")
    redirect()

