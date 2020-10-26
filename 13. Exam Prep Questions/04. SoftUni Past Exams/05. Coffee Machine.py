drink = input() # Espresso Cappuccino or Tea
sugar = input() # Without Normal or Extra
drinks_count = int(input())
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = drinks_count * 0.9
    elif sugar == "Normal":
        price = drinks_count * 1
    elif sugar == "Extra":
        price = drinks_count * 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price = drinks_count * 1
    elif sugar == "Normal":
        price = drinks_count * 1.2
    elif sugar == "Extra":
        price = drinks_count * 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = drinks_count * 0.5
    elif sugar == "Normal":
        price = drinks_count * 0.6
    elif sugar == "Extra":
        price = drinks_count * 0.7

if sugar == "Without":
    price -= price * 0.35
if drink == "Espresso" and drinks_count >= 5:
    price -= price * 0.25
if price > 15:
    price -= price * 0.2

print(f"You bought {drinks_count} cups of {drink} for {price:.2f} lv.")
