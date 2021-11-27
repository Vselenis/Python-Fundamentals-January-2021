random_words = input()

words = input()
while words != "Finish":
    command = words.split()
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        random_words = random_words.replace(current_char, new_char)
        print(random_words)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(random_words) and 0 <= end_index < len(random_words):
            random_words = random_words[:start_index] + random_words[end_index+1:]
            print(random_words)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":
        replace_chars = command[1]
        if replace_chars == "Upper":
            random_words = random_words.upper()
        elif replace_chars == "Lower":
            random_words = random_words.lower()
        print(random_words)

    elif command[0] == "Check":
        string_contains = command[1]
        if string_contains in random_words:
            print(f"Message contains {string_contains}")
        else:
            print(f"Message doesn't contain {string_contains}")

    elif command[0] == "Sum":
        starts = int(command[1])
        ends = int(command[2])
        num = 0
        if 0 <= starts < len(random_words) and 0 <= ends < len(random_words):
            for i in range(starts, ends + 1):
                num += int(ord(random_words[i]))
            print(num)
        else:
            print("Invalid indices!")



    words = input()
