budget = float(input())
destination = input() # Dubai, Sofia or London
season = input() # Summer or Winter
days = int(input())
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 45000 * days
    elif season == "Summer":
        price = 40000 * days
elif destination == "Sofia":
    if season == "Winter":
        price = 17000 * days
    elif season == "Summer":
        price = 12500 * days
elif destination == "London":
    if season == "Winter":
        price = 24000 * days
    elif season == "Summer":
        price = 20250 * days

if destination == "Dubai":
    price -= price * 0.3
elif destination == "Sofia":
    price += price * 0.25

if budget >= price:
    print(f"The budget for the movie is enough! We have {budget - price:.2f} leva left!")
else:
    print(f"The director needs {price - budget:.2f} leva more!")