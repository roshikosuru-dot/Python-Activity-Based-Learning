# Case Study 42: Student Marks Matrix Analysis

---

## 1. Problem Statement

The Student Marks Matrix Analysis program analyses student academic performance across multiple subjects using a two-dimensional matrix represented by nested lists in Python.

It calculates individual student totals and averages, identifies the top-performing student, computes subject-wise class averages, and highlights subjects whose average marks are below the specified threshold of 60%.

---

## 2. Objectives

- To represent tabular academic data using nested lists.
- To perform row-wise calculations for student totals and averages.
- To identify the highest-scoring student.
- To perform column-wise calculations for subject averages.
- To detect subjects with averages below 60%.
- To display student-wise and subject-wise performance reports.
- To practise nested loops and two-dimensional list traversal.

---

## 3. Assumptions

| S.No. | Parameter | Assumption |
|---|---|---|
| 1 | Marks Range | 0 to 100 |
| 2 | Data Structure | Two-dimensional nested list |
| 3 | Rows | Represent individual students |
| 4 | Columns | Represent individual subjects |
| 5 | Student Total | Sum of marks across all subjects |
| 6 | Student Average | Total marks divided by number of subjects |
| 7 | Subject Average | Sum of subject marks divided by number of students |
| 8 | Low Performance Threshold | Subject average below 60.0% |
| 9 | Top Performer | Student with the highest total marks |

---

## 4. Algorithm

1. Start the program.
2. Input the number of students and number of subjects.
3. Create an empty list named `subjects`.
4. Input all subject names and store them in the list.
5. Initialize empty lists named `student_names` and `marks_matrix`.
6. For each student:
   - Input the student's name.
   - Create an empty row list.
   - Input marks for each subject.
   - Validate that every mark is between 0 and 100.
   - Append each mark to the row.
   - Append the completed row to `marks_matrix`.
7. Initialize `top_total = -1` and `top_student = ""`.
8. Traverse each row of the marks matrix:
   - Calculate the student's total marks.
   - Calculate the student's average.
   - Display the student-wise performance.
   - Compare the total with `top_total`.
   - Update the top performer when a higher total is found.
9. Traverse each column of the marks matrix:
   - Calculate the total marks obtained in that subject.
   - Calculate the subject average.
   - If the average is below 60%, flag the subject as low-performing.
   - Otherwise, mark the subject as satisfactory.
10. Display the top-performing student.
11. Display the subject-wise performance report.
12. Stop the program.

---

## 5. Flowchart

```text id="c42flow"
              +----------------------+
              |        START         |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Number of      |
              | Students & Subjects  |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Subject Names  |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Student Names  |
              | and Subject Marks    |
              +----------------------+
                         |
                         v
              +----------------------+
              | Store Marks in       |
              | Nested List Matrix   |
              +----------------------+
                         |
                         v
              +----------------------+
              | Row-wise Traversal   |
              | Calculate Student    |
              | Totals & Averages    |
              +----------------------+
                         |
                         v
              +----------------------+
              | Identify Top         |
              | Performing Student   |
              +----------------------+
                         |
                         v
              +----------------------+
              | Column-wise          |
              | Traversal            |
              +----------------------+
                         |
                         v
              +----------------------+
              | Calculate Subject    |
              | Class Averages       |
              +----------------------+
                         |
                         v
                  +---------------+
                  | Average < 60?  |
                  +---------------+
                    /          \
                  Yes           No
                   |             |
                   v             v
          +----------------+  +----------------+
          | Flag as Low    |  | Mark as        |
          | Performing     |  | Satisfactory   |
          +----------------+  +----------------+
                   \             /
                    \           /
                     v         v
              +----------------------+
              | Display Complete     |
              | Matrix Analysis      |
              | Report               |
              +----------------------+
                         |
                         v
              +----------------------+
              |         END          |
              +----------------------+
```

---

## 6. Pseudocode

```text id="c42pseudo"
BEGIN

    READ num_students, num_subjects

    SET subjects = []
    SET student_names = []
    SET marks_matrix = []

    FOR j FROM 0 TO num_subjects - 1 DO

        READ subject_name
        APPEND subject_name TO subjects

    ENDFOR

    FOR i FROM 0 TO num_students - 1 DO

        READ student_name
        APPEND student_name TO student_names

        SET row = []

        FOR j FROM 0 TO num_subjects - 1 DO

            READ mark

            WHILE mark < 0 OR mark > 100 DO
                PRINT "Invalid marks"
                READ mark
            ENDWHILE

            APPEND mark TO row

        ENDFOR

        APPEND row TO marks_matrix

    ENDFOR

    SET top_total = -1
    SET top_student = ""

    FOR i FROM 0 TO num_students - 1 DO

        SET row_sum = 0

        FOR j FROM 0 TO num_subjects - 1 DO
            SET row_sum = row_sum + marks_matrix[i][j]
        ENDFOR

        SET average = row_sum / num_subjects

        PRINT student_names[i], row_sum, average

        IF row_sum > top_total THEN

            SET top_total = row_sum
            SET top_student = student_names[i]

        ENDIF

    ENDFOR

    PRINT top_student, top_total

    FOR j FROM 0 TO num_subjects - 1 DO

        SET col_sum = 0

        FOR i FROM 0 TO num_students - 1 DO
            SET col_sum = col_sum + marks_matrix[i][j]
        ENDFOR

        SET sub_avg = col_sum / num_students

        IF sub_avg < 60.0 THEN
            PRINT "LOW PERFORMANCE ALERT:", subjects[j]
        ELSE
            PRINT "SATISFACTORY:", subjects[j]
        ENDIF

    ENDFOR

END
```

---

## 7. Python Source Code

```python id="c42python"
# Case Study 42: Student Marks Matrix Analysis

# 1. Input number of students and subjects
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

# 2. Input subject names
subjects = []

for j in range(num_subjects):
    sub_name = input(
        f"Enter name of Subject {j + 1}: "
    ).strip()

    subjects.append(sub_name)

# 3. Initialize student data lists
student_names = []
marks_matrix = []

# 4. Input student names and marks
for i in range(num_students):

    name = input(
        f"\nEnter name of Student {i + 1}: "
    ).strip()

    student_names.append(name)

    row = []

    for j in range(num_subjects):

        mark = float(
            input(
                f"  Enter marks in {subjects[j]} (0-100): "
            )
        )

        # Validate marks
        while mark < 0 or mark > 100:

            print(
                "  Invalid marks! Enter a value between 0 and 100."
            )

            mark = float(
                input(
                    f"  Re-enter marks in {subjects[j]}: "
                )
            )

        row.append(mark)

    marks_matrix.append(row)

# 5. Student-wise performance analysis
print("\n================ STUDENT-WISE PERFORMANCE ================")

top_total = -1.0
top_student = ""

for i in range(num_students):

    total = 0.0

    # Calculate student total
    for j in range(num_subjects):
        total += marks_matrix[i][j]

    # Calculate student average
    avg = total / num_subjects

    print(
        f"{student_names[i]:<15} | "
        f"Total: {total:>6.1f} | "
        f"Average: {avg:>6.2f}%"
    )

    # Identify top performer
    if total > top_total:

        top_total = total
        top_student = student_names[i]

# 6. Display top performer
print("-" * 58)

print(
    f"Top Performer: {top_student} "
    f"(Total Marks: {top_total:.1f})"
)

# 7. Subject-wise performance analysis
print("\n================ SUBJECT-WISE PERFORMANCE ================")

for j in range(num_subjects):

    col_sum = 0.0

    # Calculate subject total across students
    for i in range(num_students):
        col_sum += marks_matrix[i][j]

    # Calculate subject average
    sub_avg = col_sum / num_students

    # Check performance status
    if sub_avg < 60.0:
        status = "LOW AVERAGE (<60%)"
    else:
        status = "SATISFACTORY"

    print(
        f"{subjects[j]:<15} | "
        f"Class Avg: {sub_avg:>6.2f}% | "
        f"Status: {status}"
    )

print("=" * 58)
```

---

## 8. Test Cases

**Input Details:**

- Number of Students: 3
- Number of Subjects: 3
- Subjects: Math, Physics, Python

### Student-wise Test Data

| Student Name | Math | Physics | Python | Total | Average |
|---|---:|---:|---:|---:|---:|
| Ananya | 85 | 78 | 92 | 255 | 85.00% |
| Vikram | 62 | 48 | 70 | 180 | 60.00% |
| Meera | 74 | 52 | 81 | 207 | 69.00% |

### Subject-wise Test Data

| Subject | Total Marks | Class Average | Performance |
|---|---:|---:|---|
| Math | 221 | 73.67% | Satisfactory |
| Physics | 178 | 59.33% | Low Performance |
| Python | 243 | 81.00% | Satisfactory |

### Expected Results

- **Top Performer:** Ananya
- **Highest Total:** 255 marks
- **Low-performing Subject:** Physics
- **Physics Class Average:** 59.33%

---

## 9. Sample Output

```text id="c42output"
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

---

## 10. Conclusion

The Student Marks Matrix Analysis program demonstrates how nested lists can be used to store and process structured academic data in Python.

By using row-wise and column-wise traversal, the program calculates student totals, student averages, and subject averages. It also identifies the top-performing student and detects subjects with low class averages.

This case study develops practical knowledge of two-dimensional lists, nested loops, conditional statements, aggregation, and structured data analysis in Python.
