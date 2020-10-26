budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percentage = int(input())

if nights > 7:
    price_per_night -= price_per_night * 0.05

total_price_nights = price_per_night * nights
additional_expenses = (additional_expenses_percentage / 100) * budget
total_expenses = total_price_nights + additional_expenses

if budget >= total_expenses:
    print(f"Ivanovi will be left with {budget - total_expenses:.2f} leva after vacation.")
else:
    print(f"{total_expenses - budget:.2f} leva needed.")