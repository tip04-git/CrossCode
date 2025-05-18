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

** Python **
print("Hello from Python!")

** JavaScript **
console.log("Hello from JS!");

** Bash **
echo "Hello from Bash"




