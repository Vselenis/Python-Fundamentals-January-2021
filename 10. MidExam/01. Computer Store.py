price_of_part = input()
sum_of_parts = 0
while not price_of_part.isalpha():
    if float(price_of_part) > 0:
        sum_of_parts += float(price_of_part)
    else:
        print("Invalid price!")

    price_of_part = input()

taxes = sum_of_parts * 0.2
final_price = sum_of_parts + taxes
if price_of_part.isalpha():
    if price_of_part == 'special':
        final_price = final_price * 0.9
    else:
        final_price = final_price * 1
if sum_of_parts == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_of_parts:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {final_price:.2f}$")


