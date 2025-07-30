
# 💻 CrossCode Streamlit – Multi-Language Code Execution Platform

**CrossCode Streamlit** is a web-based application that allows users to execute code in Python, JavaScript (Node.js), and Bash through an interactive Streamlit interface. This project enhances the original command-line version by providing a user-friendly graphical interface for code execution, making it ideal for learning and experimentation.


---

## 🚀 Features

- ✅ Supports three languages: **Python**, **JavaScript (Node.js)**, and **Bash**
- 🧠 Dynamically executes user code and displays output in real-time
- 📤 Captures and displays output and errors from executed scripts
- 🌐 Interactive web interface for seamless user experience
- 🛡️ Basic sandboxing via subprocess timeouts and file isolation
- ⏱️ **Set execution timeout** for code (prevents infinite loops)
- 🗂️ **Upload code files** directly for execution
- 📝 **Syntax-highlighted output and code display**
- 🕒 **Displays execution time** for each run
- 📜 **Execution history** (toggle to show/hide previous runs)
- ⚠️ **Timeout warning** if code exceeds allowed execution time


---

## 📂 Project Structure

```
crosscode-streamlit/
├── src/
│   ├── app.py          # Main entry point for the Streamlit application
│   └── utils.py        # Utility functions for executing code
├── requirements.txt     # Python dependencies
├── README.md            # You're reading it :)
└── .streamlit/
    └── config.toml     # Streamlit configuration settings
```

---

## 🧪 How It Works

1. User runs `app.py` using Streamlit.
2. Chooses a programming language: `Python`, `Bash`, or `JavaScript`.
3. Enters code in the provided text area or uploads a code file.
4. Sets the execution timeout using a slider.
5. Clicks "Execute" to run the code.
6. Output, errors, and execution time are displayed in tabs.
7. Toggle "Execution History" to view previous runs.

---

## 🛠️ Technologies Used

| Language     | Execution Tool    |
|--------------|-------------------|
| Python       | `python`          |
| JavaScript   | `node` (Node.js)  |
| Bash         | Git Bash (`bash.exe`) on Windows |
| Web Framework| Streamlit         |

---

### 📦 1. Prerequisites

- Python 3.7+
- Node.js installed (`node` command should work)
- Git Bash installed (for Bash execution on Windows)
- Streamlit installed (`pip install streamlit`)

### 🧑‍💻 2. Run the Application

```bash
streamlit run src/app.py
```

### 📝 3. Example Interaction

1. Open your web browser to the Streamlit app.
2. Select a programming language.
3. Enter your code or upload a file, set the timeout, and click "Execute".
4. View the output, errors, and execution time in the interface.
5. Toggle "Execution History" to see previous runs.

---

## ⚠️ Notes

- **Timeouts:** If your code exceeds the set timeout, execution will be stopped and a warning will be shown.
- **Sandboxing:** Code runs in isolated temporary files for safety.
- **Platform:** Bash execution requires Git Bash on Windows.
