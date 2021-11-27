n = int(input())
name = input()

current_name = []
other_name = []

for index in range(n):
    strings = input()
    current_name.append(strings)

    if name in strings:
        other_name.append(strings)

print(current_name)
print(other_name)