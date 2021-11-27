import re

pattern = r' ([a-zA-Z0-9]+[-\.\_]*[a-zA-Z0-9]+@[a-zA-Z]+-*[a-zA-Z]+([\.?][a-zA-Z]+-?[a-zA-Z]+)+)'
message = input()

matches = [x[0] for x in re.findall(pattern, message)]
print('\n'.join(matches))
