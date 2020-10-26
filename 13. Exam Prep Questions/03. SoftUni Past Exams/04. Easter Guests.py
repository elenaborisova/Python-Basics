import math
guest_count = int(input())
budget = int(input())

eggs_count = guest_count * 2
eggs_price = eggs_count * 0.45
bread_count = math.ceil(guest_count / 3)
bread_price = bread_count * 4

expenses = eggs_price + bread_price
if budget >= expenses:
    print(f"Lyubo bought {bread_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {budget - expenses:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {expenses - budget:.2f} lv. more.")
