#Basic Framework for "THE BRAIN"
# THIS: Loads the task, Sends Prompts to the LLM, Writes code to the files, Executes generated code, logs results and rewards

import json
import os
from tools.code_executor import run_code
from tools.logger import log_result
from tools.reward_system import evaluate_result


# Paths
BASE_DIR = os.path.expanduser("~/ai_dev_agent")
TASK_PATH = os.path.join(BASE_DIR, "tasks/sample_task.json")
OUTPUT_SCRIPT = os.path.join(BASE_DIR, "logs/run_001/generated_script.py")

# Mock function to simulate LLM
def generate_code(task):
    prompt = task.get("task", "Write a Python script.")
    print(f"🤖 Generating code for task: {prompt}")
    # Just returns dummy code for now
    return """print("Hello from the AI agent!")"""

def load_task(task_path):
    with open(task_path, "r") as f:
        return json.load(f)

def save_generated_code(code, path):
    with open(path, "w") as f:
        f.write(code)

def main():
    print("🚀 Agent starting...")

    # Load the task
    task = load_task(TASK_PATH)

    # Generate the code (LLM mock)
    code = generate_code(task)

    # Save code
    save_generated_code(code, OUTPUT_SCRIPT)

    # Run the code
    result = run_code(OUTPUT_SCRIPT)

    # Log result
    log_result(result, os.path.join(BASE_DIR, "logs/run_001/result.log"))
    # Evaluate reward
    reward = evaluate_result(result)
    print(f"🏆 Reward Score: {reward['score']}")
    for reason in reward['reasons']:
        print(f"  - {reason}")



    print("✅ Task complete. Check the logs for output.")

if __name__ == "__main__":
    main()
