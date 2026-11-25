# Case Study 8: Student Marks Matrix Analysis
students = ["Anu", "Balu", "Charan"]
subjects = ["Python", "Maths", "Physics"]
marks = []

for i in range(len(students)):
    row = []
    print("Enter marks for", students[i])
    for j in range(len(subjects)):
        value = int(input(subjects[j] + ": "))
        row.append(value)
    marks.append(row)

highest_total = -1
top_student = ""
for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    print(students[i], "total:", total, "average:", round(average, 2))
    if total > highest_total:
        highest_total = total
        top_student = students[i]

for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(students)):
        subject_total = subject_total + marks[i][j]
    print(subjects[j], "average:", round(subject_total / len(students), 2))

print("Top performer:", top_student)
