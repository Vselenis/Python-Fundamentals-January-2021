version = list(map(int, input().split(".")))

for x in range(len(version) - 1, -1, -1):
    if version[x] == 9:
        version[x] = 0
    else:
        version[x] += 1
        break

print(".".join([str(el) for el in version]))
