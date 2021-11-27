n = int(input())
student_academy = {}
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in student_academy:
        student_academy[student] = grade
    else:
        student_academy[student] = (student_academy[student] + grade) / 2
next_class = dict(sorted(student_academy.items(), key=lambda x: x[1], reverse=True))
for key, value in next_class.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
