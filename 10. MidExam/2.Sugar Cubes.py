the_sequence = [int(x) for x in input().split()]
sugar_cubes = input()

while sugar_cubes != "Mort":
    command = sugar_cubes.split()[0]
    value = int(sugar_cubes.split()[1])

    if command == "Add":
        the_sequence.append(value)
    elif command == "Remove":
        for val in the_sequence:
            if val == value:
                the_sequence.remove(val)
                break
    elif command == "Replace":
        replacement = int(sugar_cubes.split()[2])

        for v in range(len(the_sequence)):
            if the_sequence[v] == value:
                the_sequence.remove(value)
                the_sequence.insert(v, replacement)
                break
    elif command == "Collapse":
        the_sequence = [el for el in the_sequence if el >= value]

    sugar_cubes = input()


print(" ".join(str(z) for z in the_sequence))