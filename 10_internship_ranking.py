# Case Study 10: Multi-Criteria Internship Candidate Ranking
candidates = []
n = int(input("Number of candidates: "))

for i in range(n):
    name = input("Candidate name: ")
    marks = float(input("Academic percentage: "))
    assessment = float(input("Assessment score (out of 100): "))
    attendance = float(input("Attendance percentage: "))
    if marks >= 60 and assessment >= 50 and attendance >= 75:
        total = marks * 0.4 + assessment * 0.4 + attendance * 0.2
        candidates.append((name, total))

# Sort candidates by score in descending order using simple loops
for i in range(len(candidates)):
    for j in range(i + 1, len(candidates)):
        if candidates[j][1] > candidates[i][1]:
            temp = candidates[i]
            candidates[i] = candidates[j]
            candidates[j] = temp

print("\nEligible candidates ranked:")
for i in range(len(candidates)):
    name, score = candidates[i]
    print(i + 1, name, round(score, 2))
if len(candidates) == 0:
    print("No eligible candidates")
