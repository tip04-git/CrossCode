import subprocess

def execute_python_code(code: str, filepath: str, timeout: int):
    try:
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution timed out."

def execute_bash_command(code: str, filepath: str, timeout: int):
    bash_path = r"C:\Program Files\Git\bin\bash.exe"  # Adjust if needed
    try:
        result = subprocess.run(
            [bash_path, filepath],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution timed out."

def execute_javascript_code(code: str, filepath: str, timeout: int):
    try:
        result = subprocess.run(
            ["node", filepath],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution timed out."