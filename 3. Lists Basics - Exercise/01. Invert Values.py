n = input().split()
courses = []
for number in n:
    courses_int = int(number)
    courses_int *= -1
    courses.append(courses_int)
print(courses)