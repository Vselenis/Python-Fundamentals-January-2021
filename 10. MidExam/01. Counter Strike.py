energy = int(input())
counter = 0
distance = input()
is_winner = True
while distance != "End of battle":
    distance = int(distance)
    if energy >= distance:
        energy -= distance
        counter += 1
        if counter % 3 == 0:
            energy += counter
    else:
        is_winner = False
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break



    distance = input()

if is_winner:
    print(f"Won battles: {counter}. Energy left: {energy}")