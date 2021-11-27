targets = [int(x) for x in input().split()]
shot = input()
counter = 0
while shot != 'End':
  shot = int(shot)
  if 0 <= shot < len(targets):
    counter += 1
    for y in range(len(targets)):
      if targets[y] != -1 and targets[shot] >= targets[y] and shot != y:
        targets[y] += targets[shot]
      elif targets[y] != -1 and targets[shot] < targets[y] and shot != y:
        targets[y] -= targets[shot]
    targets[shot] = -1
  shot = input()
print(f"Shot targets: {counter} -> {' '.join(str(z) for z in targets)}")