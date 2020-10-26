days = int(input())
daily_money = 0
win_count = 0
lose_count = 0
win_days = 0
lose_days = 0
total_money = 0

for day in range(1, days + 1):
    sport = input()

    while sport != "Finish":
        result = input() # win or lose

        if result == "win":
            daily_money += 20
            win_count += 1
        elif result == "lose":
            lose_count += 1

        sport = input()

    if win_count > lose_count:
        daily_money += daily_money * 0.1
        win_days += 1
    else:
        lose_days += 1

    total_money += daily_money
    daily_money = 0
    win_count = 0
    lose_count = 0

if win_days > lose_days:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")