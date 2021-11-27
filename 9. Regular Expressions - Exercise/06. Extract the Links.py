import re

pattern = r'(w{3}\.[a-z0-9A-Z\-]+(\.[a-z]+)+)'

while True:
    line = input()
    if line:
        matches =[x[0] for x in re.findall(pattern, line)]
        for match in matches:
            print('\n'.join(matches))
    else:
        break