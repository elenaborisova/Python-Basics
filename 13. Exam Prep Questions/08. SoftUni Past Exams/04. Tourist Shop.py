budget = float(input())
product_count = 0
equipment_price = 0

product_name = input()
while product_name != "Stop":
    product_price = float(input())
    product_count += 1

    if product_count % 3 == 0:
        product_price /= 2 # or product_price -= product_price / 2

    if product_price > budget:
        print(f"You don't have enough money!")
        print(f"You need {abs(budget - product_price):.2f} leva!")
        break

    equipment_price += product_price
    budget -= product_price

    product_name = input()

if product_name == "Stop":
    print(f"You bought {product_count} products for {equipment_price:.2f} leva.")