# Case Study 2: Examination Result and Grace-Mark Validation
marks = []
subjects = ["Python", "Mathematics", "Physics"]
for subject in subjects:
    mark = int(input("Enter marks in " + subject + " (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid mark")
        mark = 0
    marks.append(mark)

grace_used = 0
for i in range(len(marks)):
    if marks[i] >= 35:
        continue
    elif marks[i] >= 32 and grace_used < 3:
        grace = 35 - marks[i]
        marks[i] = 35
        grace_used = grace_used + grace

total = sum(marks)
average = total / len(marks)
print("Final marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
if min(marks) >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
