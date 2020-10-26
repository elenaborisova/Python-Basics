import math

shooting_duration = int(input())
scenes_count = int(input())
scene_duration = int(input())

terrain_preparation = shooting_duration * 0.15
shooting_duration -= terrain_preparation
total_scene_duration = scenes_count * scene_duration

if shooting_duration >= total_scene_duration:
    print(f"You managed to finish the movie on time! You have {math.ceil(shooting_duration - total_scene_duration)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {math.ceil(total_scene_duration - shooting_duration)} minutes.")
