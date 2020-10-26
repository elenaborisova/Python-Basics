import math

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

ads = episode_duration * 0.2
episode_duration += ads
additional_last_episode_time = seasons_count * 10

total_duration = episode_duration * episodes_count * seasons_count + additional_last_episode_time

print(f"Total time needed to watch the {series_name} series is {math.floor(total_duration)} minutes.")

