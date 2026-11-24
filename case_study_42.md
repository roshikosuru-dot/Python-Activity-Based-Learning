# Case Study 42: Student Marks Matrix Analysis

## 1. Problem Statement
Analyse a 2D matrix of student marks across multiple subjects stored as a nested list, calculate row-wise (student) totals and averages, compute column-wise (subject) averages, identify top performers, and detect subjects with low average performance.

## 2. Objectives
- To represent tabular academic data using nested lists.
- To compute row-wise totals/averages and identify the highest-scoring student.
- To compute column-wise subject averages and flag subjects falling below a target threshold.

## 3. Assumptions
- Each mark is between 0 and 100.
- Row indices correspond to students, and column indices correspond to subjects.
- A subject with a class average below 60.0 is flagged as low-performing.

## 4. Algorithm
1. Start the program.
2. Input number of students num_students and number of subjects num_subjects.
3. Input subject names into a list subjects.
4. Initialize empty lists student_names and marks_matrix.
5. For each student i: input name and a list of marks across all subjects, appending the row to marks_matrix.
6. Traverse rows to calculate each student's total and average, tracking the maximum total to identify the top performer.
7. Traverse columns (j from 0 to num_subjects - 1) to sum marks across all students, compute subject averages, and flag subjects with average < 60.0.
8. Display student report, top performer, and subject-wise analysis.
9. Stop the program.

## 5. Flowchart
```text
       [ Start ]
           |
           v
/ Input num_students, num_subjects /
           |
           v
[ Populate nested list marks_matrix ]
           |
           v
[ Row Loop: Compute student totals, averages & topper ]
           |
           v
[ Column Loop: Compute subject averages & flag < 60 ]
           |
           v
 / Print Matrix Analysis Report /
           |
           v
        [ End ]
```

## 6. Pseudocode
```text
BEGIN
    READ num_students, num_subjects
    READ subjects[0..num_subjects-1]
    SET marks_matrix = []
    SET names = []

    FOR i FROM 0 TO num_students - 1 DO
        READ student_name
        APPEND student_name TO names
        SET row = []
        FOR j FROM 0 TO num_subjects - 1 DO
            READ mark
            APPEND mark TO row
        ENDFOR
        APPEND row TO marks_matrix
    ENDFOR

    SET max_total = -1
    SET topper = ""
    FOR i FROM 0 TO num_students - 1 DO
        SET row_sum = 0
        FOR j FROM 0 TO num_subjects - 1 DO
            SET row_sum = row_sum + marks_matrix[i][j]
        ENDFOR
        PRINT names[i], row_sum, row_sum / num_subjects
        IF row_sum > max_total THEN
            SET max_total = row_sum
            SET topper = names[i]
        ENDIF
    ENDFOR

    FOR j FROM 0 TO num_subjects - 1 DO
        SET col_sum = 0
        FOR i FROM 0 TO num_students - 1 DO
            SET col_sum = col_sum + marks_matrix[i][j]
        ENDFOR
        SET sub_avg = col_sum / num_students
        PRINT subjects[j], sub_avg
        IF sub_avg < 60.0 THEN
            PRINT "Low Performance Alert:", subjects[j]
        ENDIF
    ENDFOR
END
```

## 7. Python Source Code
```python
# Case Study 42: Student Marks Matrix Analysis

num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

subjects = []
for j in range(num_subjects):
    sub_name = input(f"Enter name of Subject {j + 1}: ").strip()
    subjects.append(sub_name)

student_names = []
marks_matrix = []

for i in range(num_students):
    name = input(f"\nEnter name of Student {i + 1}: ").strip()
    student_names.append(name)
    row = []
    for j in range(num_subjects):
        mark = float(input(f"  Enter marks in {subjects[j]} (0-100): "))
        while mark < 0 or mark > 100:
            print("  Invalid marks! Enter a value between 0 and 100.")
            mark = float(input(f"  Re-enter marks in {subjects[j]}: "))
        row.append(mark)
    marks_matrix.append(row)

print("
================ STUDENT-WISE PERFORMANCE ================")
top_total = -1.0
top_student = ""

for i in range(num_students):
    total = 0.0
    for j in range(num_subjects):
        total += marks_matrix[i][j]
    avg = total / num_subjects
    print(f"{student_names[i]:<15} | Total: {total:>6.1f} | Average: {avg:>6.2f}%")
    if total > top_total:
        top_total = total
        top_student = student_names[i]

print("----------------------------------------------------------")
print(f"Top Performer: {top_student} (Total Marks: {top_total:.1f})")

print("
================ SUBJECT-WISE PERFORMANCE ================")
for j in range(num_subjects):
    col_sum = 0.0
    for i in range(num_students):
        col_sum += marks_matrix[i][j]
    sub_avg = col_sum / num_students
    status = "LOW AVERAGE (<60%)" if sub_avg < 60.0 else "SATISFACTORY"
    print(f"{subjects[j]:<15} | Class Avg: {sub_avg:>6.2f}% | Status: {status}")
print("==========================================================")
```

## 8. Test Cases
- **Input:** 3 Students (`Ananya`, `Vikram`, `Meera`), 3 Subjects (`Math`, `Physics`, `Python`).
  - `Ananya`: `[85, 78, 92]` -> Total 255, Avg 85.00% (Top Performer)
  - `Vikram`: `[62, 48, 70]` -> Total 180, Avg 60.00%
  - `Meera`: `[74, 52, 81]` -> Total 207, Avg 69.00%
- **Subject Averages:** `Math`: 73.67%, `Physics`: 59.33% (**LOW AVERAGE**), `Python`: 81.00%.

## 9. Sample Output
```text
Enter number of students: 3
Enter number of subjects: 3
Enter name of Subject 1: Math
Enter name of Subject 2: Physics
Enter name of Subject 3: Python

Enter name of Student 1: Ananya
  Enter marks in Math (0-100): 85
  Enter marks in Physics (0-100): 78
  Enter marks in Python (0-100): 92

Enter name of Student 2: Vikram
  Enter marks in Math (0-100): 62
  Enter marks in Physics (0-100): 48
  Enter marks in Python (0-100): 70

Enter name of Student 3: Meera
  Enter marks in Math (0-100): 74
  Enter marks in Physics (0-100): 52
  Enter marks in Python (0-100): 81

================ STUDENT-WISE PERFORMANCE ================
Ananya          | Total:  255.0 | Average:  85.00%
Vikram          | Total:  180.0 | Average:  60.00%
Meera           | Total:  207.0 | Average:  69.00%
----------------------------------------------------------
Top Performer: Ananya (Total Marks: 255.0)

================ SUBJECT-WISE PERFORMANCE ================
Math            | Class Avg:  73.67% | Status: SATISFACTORY
Physics         | Class Avg:  59.33% | Status: LOW AVERAGE (<60%)
Python          | Class Avg:  81.00% | Status: SATISFACTORY
==========================================================
```

## 10. Conclusion
Nested list traversal enables structured row-wise and column-wise aggregation, making it straightforward to identify top-performing students and underperforming subjects.
