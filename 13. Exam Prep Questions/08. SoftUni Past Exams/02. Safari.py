budget = float(input())
gas_liters = float(input())
day = input() # Saturday or Sunday

gas_price = gas_liters * 2.10
guide_price = 100
total_price = gas_price + guide_price

if day == "Saturday":
    total_price -= total_price * 0.1
elif day == "Sunday":
    total_price -= total_price * 0.2

if budget >= total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")