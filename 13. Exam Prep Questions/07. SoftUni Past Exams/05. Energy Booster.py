fruit = input() # watermelon mango pineapple or raspberry
set_size = input() # small or big
set_count = int(input())
set_price = 0

if set_size == "small":
    if fruit == "Watermelon":
        set_price = 2 * 56
    elif fruit == "Mango":
        set_price = 2 * 36.66
    elif fruit == "Pineapple":
        set_price = 2 * 42.10
    elif fruit == "Raspberry":
        set_price = 2 * 20
elif set_size == "big":
    if fruit == "Watermelon":
        set_price = 5 * 28.70
    elif fruit == "Mango":
        set_price = 5 * 19.60
    elif fruit == "Pineapple":
        set_price = 5 * 24.80
    elif fruit == "Raspberry":
        set_price = 5 * 15.20

set_price *= set_count

if 400 <= set_price <= 1000:
    set_price -= set_price * 0.15
elif set_price > 1000:
    set_price /= 2

print(f"{set_price:.2f} lv.")
