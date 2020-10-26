mins_daily_walk = int(input())
daily_walks_count = int(input())
daily_calories = int(input())

total_mins_daily = mins_daily_walk * daily_walks_count
total_calories_burned = total_mins_daily * 5

if total_calories_burned >= 0.5 * daily_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")