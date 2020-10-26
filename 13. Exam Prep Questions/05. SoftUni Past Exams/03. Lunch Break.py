import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = 1/8 * break_duration
relax_time_duration = 1/4 * break_duration
break_duration -= lunch_duration
break_duration -= relax_time_duration

if break_duration >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(break_duration - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_duration - break_duration)} more minutes.")