# user_code.py
def format_scores(names, scores):
    exit_result = []
    for idx, (name, score) in enumerate(zip(names, scores), start=1):
        exit_result.append(f"{idx}. {name} scored {score}")
    return exit_result


# Example call (for testing)
# result = format_scores(["Alice", "Bob", "Charlie"], [85, 92, 78])
# print(result)