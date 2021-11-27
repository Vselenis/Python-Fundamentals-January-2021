character = input().split()
str_1 = character[0]
str_2 = character[1]
sum_them = 0

for i in range(max(len(str_1),len(str_2))):
    if i < len(str_1) and i < len(str_2):
        sum_them += ord(str_1[i]) * ord(str_2[i])
    else:
        if i < len(str_1):
            sum_them += ord(str_1[i])
        else:
            sum_them += ord(str_2[i])
print(sum_them)