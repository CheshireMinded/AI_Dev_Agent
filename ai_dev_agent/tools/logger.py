#The Scribe -> Logs all the action (actions, responses, errors/outputs, and reawards)

def log_result(result, log_path):
    with open(log_path, "w") as log_file:
        log_file.write("📝 Execution Log\n")
        log_file.write("=================\n")
        log_file.write(f"Success: {result['success']}\n")
        log_file.write(f"Exit Code: {result['exit_code']}\n\n")
        log_file.write("----- STDOUT -----\n")
        log_file.write(result['stdout'] + "\n")
        log_file.write("----- STDERR -----\n")
        log_file.write(result['stderr'] + "\n")
    print(f"📦 Results logged to {log_path}")
