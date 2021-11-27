import re
pattern = r'^(\$|%)([A-Z][a-z]{2,})(\1): ((\[\d*\]\|){3})$'
n = int(input())

for _ in range(n):
    text = input()
    matches = re.match(pattern, text)
    if matches == None:
        print(f"Valid message not found!")
        continue
    nums = []
    tag = matches.group(2)
    for symbol in matches.group(4).split("["):
        x = symbol[:-2]
        nums.append(x)
    my_str = ''
    for num in nums:
        if num.isdigit():
            my_str += chr(int(num))


    print(f"{tag}: {my_str}")