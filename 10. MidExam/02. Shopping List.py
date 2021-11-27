groceries = input().split('!')
command = input()

while command != "Go Shopping!":
    item = command.split()
    if item[0] == "Urgent":
        if item[1] in groceries:
            pass
        else:
            groceries.insert(0, item[1])
    elif item[0] == "Unnecessary":
        if item[1] not in groceries:
            pass
        else:
            groceries.remove(item[1])
    elif item[0] == "Correct":
        if item[1] not in groceries:
            pass
        else:
            groceries.insert(groceries.index(item[1]), item[2]), groceries.remove(item[1])
    elif item[0] == "Rearrange":
        if item[1] not in groceries:
            pass
        else:
            groceries.remove(item[1])
            groceries.append(item[1])

    command = input()

print(', '.join(groceries))
