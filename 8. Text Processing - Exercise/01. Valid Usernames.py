usernames = input().split(', ')

for el in usernames:
    if 3 <= len(el) <= 16 and (el.isalnum() or '_' in el or "-" in el):
        print(el)

