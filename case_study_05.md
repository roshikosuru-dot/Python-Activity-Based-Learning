# Case Study 31: String-Based Examination Answer Evaluation

---

## 1. Problem Statement

The String-Based Examination Answer Evaluation system compares student response strings against an official answer key. It calculates the number of correct, incorrect, and unanswered questions, applies negative marking, and generates a consolidated scorecard for all students.

The system uses character-by-character string comparison to evaluate responses and calculate student-wise scores and percentages.

---

## 2. Objectives

- To compare strings character-by-character using index-based loops.
- To identify correct answers by comparing student responses with the official answer key.
- To distinguish between correct, incorrect, and unanswered responses (`-`).
- To calculate scores using positive and negative marking.
- To calculate student-wise percentages.
- To store student results using lists and tuples.
- To display a consolidated examination scorecard.

---

## 3. Assumptions

| S.No. | Parameter | Assumption |
|---|---|---|
| 1 | Correct Answer | +4 marks |
| 2 | Incorrect Answer | -1 mark |
| 3 | Unanswered Question | 0 marks |
| 4 | Unanswered Symbol | `-` |
| 5 | Response Length | Must match the answer key length |
| 6 | Case Sensitivity | Case-insensitive comparison |
| 7 | Maximum Marks | Number of questions × 4 |
| 8 | Percentage | Net score divided by maximum marks × 100 |

---

## 4. Algorithm

1. Start the program.
2. Input the official answer key.
3. Convert the answer key into uppercase.
4. Calculate the total number of questions.
5. Calculate maximum marks by multiplying the number of questions by 4.
6. Input the number of students.
7. Initialize an empty list named `results`.
8. Repeat the following steps for each student:
   - Input the student's name.
   - Input the response string.
   - Convert the response string into uppercase.
   - Validate that its length matches the answer key.
   - If the length is incorrect, request the response again.
9. Initialize `correct`, `wrong`, and `unanswered` counters to zero.
10. Traverse the answer key using an index-based loop.
11. Compare each student response with the corresponding answer key character:
    - If the response is `-`, increment `unanswered`.
    - If the response matches the answer key, increment `correct`.
    - Otherwise, increment `wrong`.
12. Calculate the net score using:

    `Net Score = (Correct × 4) - (Wrong × 1)`

13. Calculate the percentage using:

    `Percentage = (Net Score / Maximum Marks) × 100`

14. Store the student's details and results as a tuple in the `results` list.
15. Display the consolidated examination scorecard.
16. Stop the program.

---

## 5. Flowchart

```text id="c31flow"
              +----------------------+
              |        START         |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Official       |
              | Answer Key           |
              +----------------------+
                         |
                         v
              +----------------------+
              | Calculate Total      |
              | Questions & Marks    |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Number of      |
              | Students             |
              +----------------------+
                         |
                         v
                  +-------------+
                  | Student     |
                  | Loop        |
                  +-------------+
                    /         \
                  Yes          No
                   |            |
                   v            v
          +----------------+  +-------------------+
          | Input Student  |  | Display Complete  |
          | Name & Answers |  | Scorecard         |
          +----------------+  +-------------------+
                   |                    |
                   v                    v
          +----------------+    +---------------+
          | Validate       |    |      END      |
          | Response Length|    +---------------+
          +----------------+
                   |
                   v
          +----------------------+
          | Compare Each Answer  |
          | With Answer Key      |
          +----------------------+
                   |
                   v
          +----------------------+
          | Count Correct, Wrong |
          | & Unanswered         |
          +----------------------+
                   |
                   v
          +----------------------+
          | Calculate Net Score  |
          | & Percentage         |
          +----------------------+
                   |
                   v
          +----------------------+
          | Append Result Tuple  |
          | To Results List      |
          +----------------------+
                   |
                   +------> Repeat Student Loop
```

---

## 6. Pseudocode

```text id="c31pseudo"
BEGIN

    READ answer_key
    SET answer_key = UPPERCASE(answer_key)

    SET total_q = LENGTH(answer_key)
    SET max_marks = total_q * 4
    SET results = []

    READ n

    FOR i FROM 1 TO n DO

        READ name
        READ responses
        SET responses = UPPERCASE(responses)

        WHILE LENGTH(responses) != total_q DO
            PRINT "Invalid response length"
            READ responses
            SET responses = UPPERCASE(responses)
        ENDWHILE

        SET correct = 0
        SET wrong = 0
        SET unanswered = 0

        FOR j FROM 0 TO total_q - 1 DO

            IF responses[j] == '-' THEN
                SET unanswered = unanswered + 1

            ELSE IF responses[j] == answer_key[j] THEN
                SET correct = correct + 1

            ELSE
                SET wrong = wrong + 1

            ENDIF

        ENDFOR

        SET net_score = (correct * 4) - (wrong * 1)

        SET percentage = (net_score / max_marks) * 100

        APPEND (name, correct, wrong, unanswered,
                net_score, percentage) TO results

    ENDFOR

    PRINT "EXAMINATION EVALUATION REPORT"

    FOR EACH student IN results DO

        PRINT student.name
        PRINT student.correct
        PRINT student.wrong
        PRINT student.unanswered
        PRINT student.net_score
        PRINT student.percentage

    ENDFOR

END
```

---

## 7. Python Source Code

```python
# Case Study 31: String-Based Examination Answer Evaluation

# 1. Input official answer key
answer_key = input(
    "Enter official answer key (e.g., ABCDACBD): "
).strip().upper()

total_q = len(answer_key)
max_marks = total_q * 4

# 2. Input number of students
n = int(input("Enter number of students: "))

# 3. Initialize results list
results = []

# 4. Evaluate each student's responses
for i in range(1, n + 1):

    print(f"\nStudent {i}:")

    name = input("Enter student name: ").strip()

    responses = input(
        f"Enter {total_q}-character response string "
        "(use '-' for unanswered): "
    ).strip().upper()

    # Validate response length
    while len(responses) != total_q:

        print(
            f"Invalid length! Expected {total_q} characters, "
            f"got {len(responses)}."
        )

        responses = input(
            f"Re-enter {total_q}-character response string: "
        ).strip().upper()

    # Initialize counters
    correct = 0
    wrong = 0
    unanswered = 0

    # 5. Compare answers character by character
    for j in range(total_q):

        if responses[j] == "-":
            unanswered += 1

        elif responses[j] == answer_key[j]:
            correct += 1

        else:
            wrong += 1

    # 6. Calculate score and percentage
    net_score = (correct * 4) - (wrong * 1)

    percentage = (net_score / max_marks) * 100

    # 7. Store student result as a tuple
    results.append(
        (name, correct, wrong, unanswered, net_score, percentage)
    )

# 8. Display consolidated examination report
print(
    "\n==================== EXAMINATION EVALUATION REPORT "
    "===================="
)

print(
    f"Answer Key: {answer_key} | "
    f"Total Questions: {total_q} | "
    f"Max Marks: {max_marks}"
)

print("-" * 71)

print(
    "Name            | Correct | Wrong | Skipped | "
    "Net Score | Percentage"
)

print("-" * 71)

# 9. Display each student's result
for name, correct, wrong, unanswered, net_score, percentage in results:

    print(
        f"{name:<15} | "
        f"{correct:^7} | "
        f"{wrong:^5} | "
        f"{unanswered:^7} | "
        f"{net_score:^9} | "
        f"{percentage:>8.2f}%"
    )

print("=" * 71)
```

---

## 8. Test Cases

**Official Answer Key:** `ABCDAC`

**Total Questions:** 6

**Maximum Marks:** 24

| Test Case | Student | Responses | Correct | Wrong | Skipped | Net Score | Percentage |
|---|---|---|---:|---:|---:|---:|---:|
| 1 | Aarav | `ABCDAC` | 6 | 0 | 0 | 24 | 100.00% |
| 2 | Diya | `AB-DA-` | 4 | 0 | 2 | 16 | 66.67% |
| 3 | Rohan | `ABBBBC` | 3 | 3 | 0 | 9 | 37.50% |

### Score Calculation

**Test Case 1 – Aarav**

- Correct: 6
- Wrong: 0
- Skipped: 0
- Net Score = (6 × 4) − (0 × 1) = **24**
- Percentage = (24 / 24) × 100 = **100.00%**

**Test Case 2 – Diya**

- Correct: 4
- Wrong: 0
- Skipped: 2
- Net Score = (4 × 4) − (0 × 1) = **16**
- Percentage = (16 / 24) × 100 = **66.67%**

**Test Case 3 – Rohan**

- Correct: 3
- Wrong: 3
- Skipped: 0
- Net Score = (3 × 4) − (3 × 1) = **9**
- Percentage = (9 / 24) × 100 = **37.50%**

---

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
Enter 6-character response string (use '-' for unanswered): ABBBB C

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

---

## 10. Conclusion

The String-Based Examination Answer Evaluation system demonstrates character-by-character string comparison, index-based loops, conditional statements, negative marking, and list-based data storage in Python.

It accurately classifies correct, incorrect, and unanswered responses, calculates student-wise scores and percentages, and generates a consolidated examination report.

This case study provides practical knowledge of string processing, tuple storage, loops, arithmetic operations, and formatted output in Python.
