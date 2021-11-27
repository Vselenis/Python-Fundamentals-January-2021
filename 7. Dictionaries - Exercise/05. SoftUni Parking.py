n = int(input())
parking = {}

for _ in range(n):
  word = input().split()
  command = word[0]
  username = word[1]
  if command == "register":
    number = word[2]
    if username not in parking:
      parking[username] = number
      print(f"{username} registered {number} successfully")
    else:
      print(f"ERROR: already registered with plate number {number}")
  elif command == "unregister":
    if username not in parking:
      print(f"ERROR: user {username} not found")
    else:
      parking.pop(username)
      print(f"{username} unregistered successfully")
for key, value in parking.items():
  print(f"{key} => {value}")
