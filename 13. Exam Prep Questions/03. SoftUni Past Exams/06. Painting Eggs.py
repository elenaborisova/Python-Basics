egg_size = input() # Large Medium or Small
egg_color = input() # Red Green or Yellow
egg_basket_count = int(input())
price_per_basket = 0

if egg_color == "Red":
    if egg_size == "Large":
        price_per_basket = 16
    elif egg_size == "Medium":
        price_per_basket = 13
    elif egg_size == "Small":
        price_per_basket = 9
elif egg_color == "Green":
    if egg_size == "Large":
        price_per_basket = 12
    elif egg_size == "Medium":
        price_per_basket = 9
    elif egg_size == "Small":
        price_per_basket = 8
elif egg_color == "Yellow":
    if egg_size == "Large":
        price_per_basket = 9
    elif egg_size == "Medium":
        price_per_basket = 7
    elif egg_size == "Small":
        price_per_basket = 5

total_egg_basket_price = price_per_basket * egg_basket_count
expenses = total_egg_basket_price * 0.35
profit = total_egg_basket_price - expenses

print(f"{profit:.2f} leva.")