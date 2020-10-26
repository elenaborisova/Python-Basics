days = int(input())
hours = int(input())
total_parking_fee = 0
daily_parking_fee = 0

for day in range(1, days + 1):
    daily_parking_fee = 0
    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0: # even day and odd hour
            parking_fee = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_fee = 1.25
        else:
            parking_fee = 1

        total_parking_fee += parking_fee
        daily_parking_fee += parking_fee

    print(f"Day: {day} - {daily_parking_fee:.2f} leva")

print(f"Total: {total_parking_fee:.2f} leva")