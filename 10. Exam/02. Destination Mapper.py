import re

pattern = r'(=|/)([A-Z][a-zA-Z]{2,})(\1)'
text = input()

destination = [match for _, match, _ in re.findall(pattern, text)]

travel_points = [len(match) for _, match, _ in re.findall(pattern, text)]

print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {sum(travel_points)}")