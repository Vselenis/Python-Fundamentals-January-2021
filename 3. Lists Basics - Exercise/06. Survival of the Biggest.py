import sys
string = input().split()
n = int(input())
course = []
for symbol in string:
    goint = int(symbol)
    course.append(goint)
for index in range(n):
    min_number = sys.maxsize

    for i in course:
        number = int(i)
        if number < min_number:
            min_number = number
    course.remove(min_number)

print(course)