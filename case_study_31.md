# Case Study 31: String-Based Examination Answer Evaluation

## 1. Problem Statement
Compare student answer strings against an official answer key string, calculate correct, incorrect, and unanswered responses, apply negative marking, and produce student-wise results.

## 2. Objectives
- To compare strings character-by-character using index-based loops.
- To distinguish between correct answers, incorrect answers, and skipped questions ('-').
- To compute net scores with negative marking and store student summaries in lists.

## 3. Assumptions
- Each question carries +4 marks for a correct answer, -1 mark for an incorrect answer, and 0 marks for an unanswered question ('-').
- All student response strings have the exact same length as the answer key.
- Inputs are case-insensitive ('a' and 'A' are treated identically).

## 4. Algorithm
1. Start the program.
2. Input the official answer key string key and convert to uppercase.
3. Input the number of students n.
4. Initialize an empty list results.
5. For each student from 1 to n: input student name and response string ans (converted to uppercase).
6. Validate that len(ans) == len(key).
7. Initialize correct = 0, wrong = 0, unanswered = 0.
8. Loop index j from 0 to len(key) - 1: if ans[j] == '-', increment unanswered; else if ans[j] == key[j], increment correct; else increment wrong.
9. Calculate score = (correct * 4) - (wrong * 1) and percentage = (score / (len(key) * 4)) * 100.
10. Store student result tuple in results and print the complete scorecard.
11. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
 / Input Answer Key /
           |
           v
 / Input n students /
           |
           v
  < Student Loop > ---- No ----> [ Display Consolidated Scorecard ]
           |                                      |
          Yes                                     v
           |                                   [ End ]
           v
 / Input Name & Response /
           |
           v
[ Loop j = 0 to len(key)-1: Compare ans[j] vs key[j] ]
           |
           v
[ Score = Correct*4 - Wrong*1 ]
           |
           v
[ Append Result Tuple & Repeat ]
```

## 6. Pseudocode
```text
BEGIN
    READ key
    SET key = UPPERCASE(key)
    SET total_q = LENGTH(key)
    SET max_marks = total_q * 4
    SET results = []

    READ n
    FOR i FROM 1 TO n DO
        READ name, ans
        SET ans = UPPERCASE(ans)
        SET correct = 0, wrong = 0, skipped = 0

        FOR j FROM 0 TO total_q - 1 DO
            IF ans[j] == '-' THEN
                SET skipped = skipped + 1
            ELSE IF ans[j] == key[j] THEN
                SET correct = correct + 1
            ELSE
                SET wrong = wrong + 1
            ENDIF
        ENDFOR

        SET score = (correct * 4) - (wrong * 1)
        APPEND (name, correct, wrong, skipped, score) TO results
    ENDFOR

    FOR EACH (name, c, w, s, sc) IN results DO
        PRINT name, c, w, s, sc
    ENDFOR
END
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
- **Answer Key:** `ABCDAC` (6 questions, Max Marks = 24)
- **Test Case 1 (Aarav):** `ABCDAC` -> 6 Correct, 0 Wrong, 0 Skipped -> Net Score = **24** (100.00%).
- **Test Case 2 (Diya):** `AB-DA-` -> 4 Correct, 0 Wrong, 2 Skipped -> Net Score = **16** (66.67%).
- **Test Case 3 (Rohan):** `ABBBBC` -> 3 Correct, 3 Wrong, 0 Skipped -> Net Score = 12 - 3 = **9** (37.50%).

## 9. Sample Output
```text
Enter official answer key (e.g., ABCDACBD): ABCDAC
Enter number of students: 3

Student 1:
Enter student name: Aarav
Enter 6-character response string (use '-' for unanswered): ABCDAC

Student 2:
Enter student name: Diya
Enter 6-character response string (use '-' for unanswered): AB-DA-

Student 3:
Enter student name: Rohan
Enter 6-character response string (use '-' for unanswered): ABBBBC

==================== EXAMINATION EVALUATION REPORT ====================
Answer Key: ABCDAC | Total Questions: 6 | Max Marks: 24
-----------------------------------------------------------------------
Name            | Correct | Wrong | Skipped | Net Score | Percentage
-----------------------------------------------------------------------
Aarav           |    6    |   0   |    0    |    24     |   100.00%
Diya            |    4    |   0   |    2    |    16     |    66.67%
Rohan           |    3    |   3   |    0    |     9     |    37.50%
=======================================================================
```

## 10. Conclusion
The evaluation system reliably grades OMR-style response strings using parallel indexing, enforces negative marking rules, and presents tabular results via tuple unpacking.
