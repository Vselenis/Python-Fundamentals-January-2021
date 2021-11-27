command = input()

while command != "Done":
    command = command.split()
    if command[0] == 'TakeOdd':
        password = [password[i] for i in range(len(password)) if i % 2 == 1]
        password = ''.join(password)
        print(password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = (index + int(command[2]))
        first_half = password[0: index]
        second_half = password[length: len(password)]
        password = first_half+ second_half
        print(password)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")