targets = [int(x) for x in input().split()]
command = input()

while command != "End":
  do, index, power = command.split()
  index = int(index)
  power = int(power)
  if do == "Shoot":
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
  elif do == "Add":
    if 0 <= index < len(targets):
      targets.insert(index, power)
    else:
      print("Invalid placement!")
  elif do == "Strike":
    x = index - power
    y = index + power
    if 0 <= x and y < len(targets):
      del targets[x:y+1]
    else:
      print("Strike missed!")
  command = input()

print("|".join(str(z) for z in targets))