month = input() # march april may june july or august
hours = int(input())
people_count = int(input())
day_or_night = input()
price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price_per_hour = 10.50
    elif day_or_night == "night":
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price_per_hour = 12.60
    elif day_or_night == "night":
        price_per_hour = 10.20

if people_count >= 4:
    price_per_hour *= 0.9
if hours >= 5:
    price_per_hour *= 0.5

total_price = price_per_hour * hours * people_count

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")