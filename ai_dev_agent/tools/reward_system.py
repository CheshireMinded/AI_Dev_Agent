#The Teacher -> Calculates the reward scores based upon success/failures and runtime behaviors

def evaluate_result(execution_result):
    score = 0
    reasons = []

    # Reward for successful execution
    if execution_result['success']:
        score += 10
        reasons.append("Script executed successfully.")
    else:
        score -= 5
        reasons.append("Script failed to execute.")

    # Reward or penalize based on stderr
    if execution_result['stderr']:
        score -= 2
        reasons.append("Script produced errors.")

    # Bonus: output something meaningful
    if "hello" in execution_result['stdout'].lower():
        score += 2
        reasons.append("Output contained 'hello' — assumed task success.")

    return {
        "score": score,
        "reasons": reasons
    }
