import math

employees_count = int(input())
entrance_fee = float(input())
chair_price = float(input())
umbrella_price = float(input())

total_chair_price = math.ceil(employees_count * 0.75) * chair_price
total_umbrella_price = math.ceil(employees_count / 2) * umbrella_price
total_expenses = (employees_count * entrance_fee) + total_chair_price + total_umbrella_price

print(f"{total_expenses:.2f} lv.")
