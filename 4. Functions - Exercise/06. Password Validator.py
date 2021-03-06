def validator(password):
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    is_not_digit = False
    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
    counter_digits = 0
    for el in password:
        if el.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid

password = input()
is_valid = validator(password)
if is_valid:
    print('Password is valid')