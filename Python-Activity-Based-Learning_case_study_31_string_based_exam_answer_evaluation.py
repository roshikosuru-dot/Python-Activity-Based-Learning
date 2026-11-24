# Case Study 31: String-Based Examination Answer Evaluation

answer_key = input("Enter official answer key (e.g., ABCDACBD): ").strip().upper()
total_q = len(answer_key)
max_marks = total_q * 4

n = int(input("Enter number of students: "))
results = []

for i in range(1, n + 1):
    print(f"\nStudent {i}:")
    name = input("Enter student name: ").strip()
    responses = input(f"Enter {total_q}-character response string (use '-' for unanswered): ").strip().upper()

    while len(responses) != total_q:
        print(f"Invalid length! Expected {total_q} characters, got {len(responses)}.")
        responses = input(f"Re-enter {total_q}-character response string: ").strip().upper()

    correct = 0
    wrong = 0
    unanswered = 0

    for j in range(total_q):
        if responses[j] == "-":
            unanswered += 1
        elif responses[j] == answer_key[j]:
            correct += 1
        else:
            wrong += 1

    net_score = (correct * 4) - (wrong * 1)
    percentage = (net_score / max_marks) * 100
    results.append((name, correct, wrong, unanswered, net_score, percentage))

print("
==================== EXAMINATION EVALUATION REPORT ====================")
print(f"Answer Key: {answer_key} | Total Questions: {total_q} | Max Marks: {max_marks}")
print("-----------------------------------------------------------------------")
print("Name            | Correct | Wrong | Skipped | Net Score | Percentage")
print("-----------------------------------------------------------------------")
for name, correct, wrong, unanswered, net_score, percentage in results:
    print(f"{name:<15} | {correct:^7} | {wrong:^5} | {unanswered:^7} | {net_score:^9} | {percentage:>8.2f}%")
print("=======================================================================")
