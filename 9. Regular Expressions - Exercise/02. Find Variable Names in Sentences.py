import re

pattern = r'\b_[0-9a-zA-Z]+\b'
text = input()

matches = [x.replace('_', '') for x in re.findall(pattern, text)]


print(','.join(matches))
