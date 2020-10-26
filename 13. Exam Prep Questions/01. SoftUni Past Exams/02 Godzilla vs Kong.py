budget = float(input())
people_count = int(input())
equipment_price = float(input())

decor = 0.1 * budget
total_equipment_price = people_count * equipment_price

if people_count > 150:
    total_equipment_price -= total_equipment_price * 0.1

total_expenses = decor + total_equipment_price

if total_expenses > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_expenses - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_expenses:.2f} leva left.")