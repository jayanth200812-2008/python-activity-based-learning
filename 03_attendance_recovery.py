# Case Study 3: Attendance Recovery Computation
held = int(input("Classes held so far: "))
attended = int(input("Classes attended so far: "))
target = float(input("Required attendance percentage: "))

if held <= 0 or attended < 0 or attended > held or target <= 0 or target > 100:
    print("Invalid input")
else:
    current = attended * 100 / held
    print("Current attendance:", round(current, 2), "%")
    required = 0
    while (attended + required) * 100 / (held + required) < target:
        required = required + 1
    print("Consecutive classes to attend:", required)
