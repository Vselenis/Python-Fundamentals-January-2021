import re

pattern = '\\b[A-Z][a-z]+[ ][A-Z][a-z]+\\b'
text = input()
matches = re.findall(pattern, text)
print(' '.join(matches))