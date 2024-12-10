import os
import subprocess

current_mode = "text"

def new_file(filename):
    with open(filename, 'w') as file:
        print("New file created:", filename)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("File not found.")

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print("File saved:", filename)

def run_script(name: str, isUtility: bool):
    if isUtility == True:
        pass
    else:
        with open('fileToBeRunName.txt', "w") as file:
            pass
    
        with open('fileToBeRunName.txt', "w") as file:
            file.write(name)
    
        
    print("Running script...")
    if os.name == 'nt':  # For Windows
        subprocess.run(['runFileWindows.bat'], shell=True)
    elif os.name == 'posix': 
        if 'darwin' in os.uname().sysname.lower():  # For macOS
            subprocess.run(['./runFilemacOS.command'], shell=True)
        else:  # For Linux
            subprocess.run(['./runFileLinux.sh'], shell=True)
    else:
        print("Unsupported OS")
    print("Script run completed.")

def main():
    clear()
    global current_mode
    print("PyPad - The smallest possible Python IDE")
    while True:
        print(f"Current mode: {current_mode}")
        if current_mode == "text":
            command = input("Enter command (new/open/save/run/exit/comand): ")
            
            if command == 'new':
                filename = input("Enter filename: ")
                new_file(filename)
            
            elif command == 'open':
                filename = input("Enter filename: ")
                open_file(filename)
            
            elif command == 'save':
                filename = input("Enter filename: ")
                print("Enter file content (type 'EOF' on a new line to finish and type 'cmd' to enter comand mode):")
                content = ""
                while True:
                    line = input()
                    if line == 'EOF':
                        break
                    if line == 'cmd':
                        current_mode = "comand"
                        clear()
                    content += line + '\n'
                save_file(filename, content)
            
            elif command == 'run':
                script_name = input("Enter script name to run: ")
                clear()
                run_script(script_name)
            
            elif command == 'exit':
                print("Exiting PyPad...")
                break
            
            elif command == 'comand':
                current_mode = "comand"
                clear()
            
            else:
                print("Invalid command.")
        
        elif current_mode == "comand":
            clear()
            current_mode = "comand"
    
    if current_mode == "text":
        pass
    elif current_mode == "command":
        run_script("comand.py", True)
        

if __name__ == "__main__":
    main()

