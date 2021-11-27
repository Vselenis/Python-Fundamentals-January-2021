note = input()
tasks = []

while not note == 'End':
    data = note.split('-')
    importance = int(data[0])
    task = data[1]
    tasks.append((importance, task))
    note = input()

tasks_in_priority = [task_name for importance, task_name in sorted(tasks)] 
print(tasks_in_priority)
