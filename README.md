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
# CrossCode 

CrossCode is a unified, cross-language compiler that allows users to write and execute Python, JavaScript, and Bash code from a single platform. Designed with flexibility in mind, this tool streamlines multi-language development without requiring external dependencies on the user’s system.

---

## 🚀 Features

- ✅ Run Python, JavaScript (via V8), and Bash scripts
- ✅ Web interface to input code and select language
- ✅ Unified execution backend using C++ and system calls
- ✅ Safe and isolated runtime environment
- ✅ Built for web integration with a Node.js + Express backend

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (React planned)
- **Backend:** Node.js + Express.js
- **Languages Supported:** Python, JavaScript (via V8), Bash
- **Compiler Core:** C++ (handles multi-language execution)
- **Platform:** AWS (free-tier hosting)

---


---

## 🔧 How It Works

1. User selects a language and enters code via the frontend.
2. Backend sends the code to the C++ core engine.
3. The code is executed using:
   - **Python interpreter**
   - **V8 for JavaScript**
   - **MinGW/Bash for shell scripts**
4. Output is captured and sent back to frontend.

---

## Example Use Case

Python: print("Hello from Python!")

JavaScript : console.log("Hello from JS!");

Bash : echo "Hello from Bash"





