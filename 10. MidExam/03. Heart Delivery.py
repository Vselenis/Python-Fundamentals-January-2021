houses = [int(el) for el in input().split('@')]
lets_jump = input()
position = 0

while lets_jump != "Love!":
    length = lets_jump.split()[1]
    position += int(length)
    if position >= len(houses):
        position = 0


    if houses[position] > 0:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day.")

    elif houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")

    lets_jump = input()
print(f"Cupid's last position was {position}.")

if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len([house for house in houses if house > 0])} places.")