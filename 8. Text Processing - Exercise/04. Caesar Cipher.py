text = input()
encrypted_version = ''
for index in text:
    encrypted_version += chr(ord(index) + 3)

print(encrypted_version)