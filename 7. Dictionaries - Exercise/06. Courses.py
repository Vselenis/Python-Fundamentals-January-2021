command = input()
dict_name = {}

while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in dict_name:
        dict_name[course_name] = [student_name]
    else:
        dict_name[course_name] += [student_name]
    command = input()

new_dict = dict(sorted(dict_name.items(), key = lambda x: len(x[1]), reverse=True))

for course, students in new_dict.items():
    print(f"{course}: {len(students)}")
    sort_students = sorted(students)
    for student in sort_students:
        print(f"-- {student}")
