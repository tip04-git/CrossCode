import streamlit as st
import tempfile
import os
from utils import execute_python_code, execute_bash_command, execute_javascript_code

EXAMPLES_FOR_TIMING = {
    "Python": 'import time\nstart = time.time()\nfor i in range(1000000): pass\nprint("Elapsed:", time.time() - start)',
    "JavaScript": 'const start = Date.now();\nfor (let i = 0; i < 1000000; i++) {}\nconsole.log("Elapsed:", (Date.now() - start)/1000);',
    "Bash": 'start=$(date +%s)\nfor i in {1..1000000}; do :; done\nend=$(date +%s)\necho "Elapsed: $((end-start)) seconds"'
}

if "history" not in st.session_state:
    st.session_state["history"] = []

# ...existing code...

def main():
    st.title("CrossCode – Multi-Language Code Execution Platform")

    language = st.selectbox("Select the programming language:", ["Python", "Bash", "JavaScript"])

    uploaded_file = st.file_uploader("Or upload a code file", type=["py", "js", "sh"])
    user_code = ""
    if uploaded_file:
        user_code = uploaded_file.read().decode()
        st.text_area("Your uploaded code:", user_code, height=200, disabled=True)
    else:
        user_code = st.text_area("Enter your code below:", value="", height=200)

    timeout = st.slider("Execution timeout (seconds)", min_value=1, max_value=10, value=5)

    import time
# ...existing imports...

    if st.button("Execute"):
        if not user_code.strip():
            st.warning("Please enter or upload code.")
            return

        with tempfile.NamedTemporaryFile(delete=False, suffix={
            "Python": ".py", "JavaScript": ".js", "Bash": ".sh"
        }[language]) as temp_file:
            temp_file.write(user_code.encode())
            temp_file.flush()
            temp_path = temp_file.name

        start_time = time.time()
        try:
            if language == "Python":
                output, error = execute_python_code(user_code, temp_path, timeout)
            elif language == "Bash":
                output, error = execute_bash_command(user_code, temp_path, timeout)
            elif language == "JavaScript":
                output, error = execute_javascript_code(user_code, temp_path, timeout)
        finally:
            os.remove(temp_path)
        end_time = time.time()
        exec_time = end_time - start_time

        st.session_state["history"].append({
            "language": language,
            "code": user_code,
            "output": output,
            "error": error,
            "exec_time": exec_time
        })

        tab1, tab2 = st.tabs(["Output", "Error"])
        with tab1:
            st.code(output or "No output.", language=language.lower())
            st.markdown(f"**Execution Time:** {exec_time:.3f} seconds")
        with tab2:
            st.code(error or "No error.", language=language.lower())

        st.markdown("**Your code:**")
        st.code(user_code, language=language.lower())
        if error and "timed out" in error.lower():
            st.warning("Your code exceeded the execution timeout and was stopped.")

    show_history = st.checkbox("Execution History")
    if show_history:
        st.subheader("Execution History")
        for i, entry in enumerate(reversed(st.session_state["history"][-5:]), 1):
            st.markdown(f"**{entry['language']}**")
            st.code(entry["code"], language=entry["language"].lower())
            st.markdown("**Output:**")
            st.code(entry["output"] or "No output.", language=entry["language"].lower())
            st.markdown(f"**Execution Time:** {entry.get('exec_time', 0):.3f} seconds")
            st.markdown("**Error:**")
            st.code(entry["error"] or "No error.", language=entry["language"].lower())
            st.markdown("---")

if __name__ == "__main__":
    main()