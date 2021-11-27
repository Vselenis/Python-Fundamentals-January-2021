gifts = input().split()
command = input()
while command != 'No Money':
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == current_gift:
                gifts[i] = 'None'
    if current_command[0] == 'Required':
        value = int(current_command[2])
        if 0 <= value < len(gifts):
            gifts[value] = current_gift
    if current_command[0] == 'JustInCase':
        gifts[-1] = current_gift

    command = input()

for gift in gifts:
    if gift != 'None':
        print(gift, end=' ')
