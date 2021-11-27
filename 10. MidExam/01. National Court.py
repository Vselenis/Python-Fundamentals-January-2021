employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

total_people = int(input())

people_per_hour = employee_1 + employee_2 + employee_3
count = 0
breaking_time = 0
while total_people > 0:
    count += 1
    total_people -= people_per_hour
    if count % 3 == 0 and total_people > 0:
        breaking_time += 1

print(f"Time needed: {breaking_time+count}h.")