destination = input()

command = input()

while command != 'Travel':
    command = command.split(":")
    if command[0] == "Add Stop":
        i = int(command[1])
        new_destination = command[2]
        if 0 <= i < len(destination):
            destination = destination[:i] + new_destination + destination[i:]
        print(destination)
    elif command[0] == "Remove Stop":
        index_1 = int(command[1])
        index_2 = int(command[2]) + 1
        if 0 <= index_1 <= index_2 <= len(destination):
            destination = destination[:index_1] + destination[index_2:]
        print(destination)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in destination:
            destination = destination.replace(old_string, new_string)
        print(destination)



    command = input()

print(f"Ready for world tour! Planned stops: {destination}")