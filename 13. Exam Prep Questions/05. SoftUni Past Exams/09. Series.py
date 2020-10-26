budget = float(input())
series_count = int(input())
total_series_price = 0

for series in range(1, series_count + 1):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price -= series_price * 0.5
    elif series_name == "Lucifer":
        series_price -= series_price * 0.4
    elif series_name == "Protector":
        series_price -= series_price * 0.3
    elif series_name == "TotalDrama":
        series_price -= series_price * 0.2
    elif series_name == "Area":
        series_price -= series_price * 0.1

    total_series_price += series_price

if budget >= total_series_price:
    print(f"You bought all the series and left with {budget - total_series_price:.2f} lv.")
else:
    print(f"You need {total_series_price - budget:.2f} lv. more to buy the series!")
