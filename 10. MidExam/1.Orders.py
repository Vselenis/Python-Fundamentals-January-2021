count_of_orders = int(input())
total_price = 0

for _ in range(count_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    count_capsule = int(input())
    cofee_price = price_per_capsule * days * count_capsule
    print(f"The price for the coffee is: ${cofee_price:.2f}")
    total_price += cofee_price
print(f"Total: ${total_price:.2f}")