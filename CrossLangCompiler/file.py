import subprocess
import os

def execute_python_code(code: str):
    """Execute Python code."""
    with open("temp.py", "w") as file:
        file.write(code)
    
    # Debug print
    print("Executing Python code...")

    # Execute the Python script and capture output
    result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
    print(f"Python Execution Return Code: {result.returncode}")
    print("Python Execution Output:", result.stdout)
    if result.stderr:
        print("Python Execution Error:", result.stderr)

def execute_bash_command(command: str):
    """Execute a Bash command using Git Bash."""
    print("Executing Bash command...")

    # Path to Git Bash's bash.exe
    bash_path = r"C:\Program Files\Git\bin\bash.exe"  # Adjust the path if needed
    result = subprocess.run([bash_path, "-c", command], capture_output=True, text=True)

    print(f"Bash Execution Return Code: {result.returncode}")
    print("Bash Execution Output:", result.stdout)
    if result.stderr:
        print("Bash Execution Error:", result.stderr)

def execute_javascript_code(code: str):
    """Execute JavaScript code using Node.js."""
    with open("temp.js", "w") as file:
        file.write(code)
    
    # Debug print
    print("Executing JavaScript code...")

    # Execute the JavaScript file using Node.js and capture output
    result = subprocess.run(["node", "temp.js"], capture_output=True, text=True)
    print(f"JavaScript Execution Return Code: {result.returncode}")
    print("JavaScript Execution Output:", result.stdout)
    if result.stderr:
        print("JavaScript Execution Error:", result.stderr)

def get_user_input():
    """Prompt user for language and code."""
    print("Welcome to the Cross-Language Compiler!")
    
    # Get user input for language
    language = input("Enter the programming language (python/bash/js): ").lower()
    
    if language not in ["python", "bash", "js"]:
        print("Invalid language choice! Please choose from 'python', 'bash', or 'js'.")
        return
    
    # Get code input from the user
    print(f"Enter your {language} code below (type 'exit' to finish):")
    user_code = ""
    
    while True:
        line = input()
        if line.lower() == "exit":
            break
        user_code += line + "\n"
    
    # Execute the code based on language
    if language == "python":
        execute_python_code(user_code)
    elif language == "bash":
        execute_bash_command(user_code)
    elif language == "js":
        execute_javascript_code(user_code)

def main():
    get_user_input()

if __name__ == "__main__":
    main()
