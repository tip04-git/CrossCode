# 💻 CrossCode – Multi-Language Code Execution Platform (CLI Version)

**CrossCode** is a lightweight command-line code execution system that supports running Python, JavaScript (Node.js), and Bash code on the fly — all from a unified CLI interface. It simulates a basic interpreter environment using subprocesses, making it ideal for learning, prototyping, and multi-language code experimentation.

---

## 🚀 Features

- ✅ Supports three languages: **Python**, **JavaScript (Node.js)**, and **Bash**
- 🧠 Dynamically generates and executes user code via temp files
- 📤 Captures and displays output and errors from executed scripts
- 🔁 Command-line interface (CLI) for interactive input
- 🛡️ Basic sandboxing via subprocess timeouts and file isolation

---

## 📂 Project Structure

```
CrossCode/
├── file.py # Core Python script for CLI execution
├── requirements.txt # Python dependencies (optional for now)
├── README.md # You're reading it :)

```


---

## 🧪 How It Works

1. User runs `file.py`
2. Chooses language: `python`, `bash`, or `js`
3. Enters code (multi-line, ends with `exit`)
4. Code is written to a temp file
5. Subprocess runs the file using the correct interpreter
6. Output and errors are displayed in the terminal

---

## 🛠️ Technologies Used

| Language     | Execution Tool    |
|--------------|-------------------|
| Python       | `python`          |
| JavaScript   | `node` (Node.js)  |
| Bash         | Git Bash (`bash.exe`) on Windows |

---

## ▶️ Usage (CLI)

### 📦 1. Prerequisites

- Python 3.7+
- Node.js installed (`node` command should work)
- Git Bash installed (for Bash execution on Windows)

### 🧑‍💻 2. Run the Script

```bash
python file.py
```

### 📝 3. Example Interaction

```bash
Welcome to the Cross-Language Compiler!
Enter the programming language (python/bash/js): python
Enter your python code below (type 'exit' to finish):
print("Hello from Python!")
exit

Executing Python code...
Python Execution Output: Hello from Python!


