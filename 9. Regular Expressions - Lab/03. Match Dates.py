import re

pattern = r'(\d{2})([.\-/])([A-Z][a-z]{2})\2(\d{4})'
text = input()

matches = re.findall(pattern, text)

for (day, _, month, year) in matches:
    print(f'Day: {day}, Month: {month}, Year: {year}')
