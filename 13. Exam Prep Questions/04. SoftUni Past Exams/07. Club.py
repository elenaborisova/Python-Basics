target_profit = float(input())
cocktail_price = 0
total_profit = 0

cocktail_name = input()
while cocktail_name != "Party!":
    cocktails_count = int(input())
    cocktail_price = len(cocktail_name)
    order_price = cocktail_price * cocktails_count

    if order_price % 2 != 0:
        order_price -= order_price * 0.25

    total_profit += order_price
    if total_profit >= target_profit:
        print(f"Target acquired.")
        break

    order_price = 0

    cocktail_name = input()

if cocktail_name == "Party!":
    print(f"We need {target_profit - total_profit:.2f} leva more.")

print(f"Club income - {total_profit:.2f} leva.")