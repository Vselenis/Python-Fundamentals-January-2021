cards = input().split()
index = input()
counter = 0
while index != 'end' and cards:
    counter += 1
    x, y = [int(el) for el in index.split()]

    if len(cards) == 0:
        print(f"You have won in {counter - 1} turns!")
        break

    if x == y or x not in range(len(cards)) or y not in range(len(cards)):
        half_list = len(cards) // 2
        cards.insert(int(half_list), f"-{counter}a")
        cards.insert(int(half_list) + 1, f"-{counter}a")
        print("Invalid input! Adding additional elements to the board")


    elif cards[x] == cards[y]:
        element = cards[x]
        print(f'Congrats! You have found matching elements - {cards[x]}!')
        cards.remove(element)
        cards.remove(element)


    elif cards[x] != cards[y]:
        print("Try again!")

    index = input()

if not cards:
    print(f"You have won in {counter} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(cards))

