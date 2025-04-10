#The Hands -> creates the subprocesses

import subprocess

def run_code(script_path):
    try:
        print(f"🛠️  Running generated script: {script_path}")
        result = subprocess.run(
            ["python3", script_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": "Script timed out.",
            "exit_code": -1
        }

    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1
        }
