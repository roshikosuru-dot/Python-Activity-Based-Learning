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
