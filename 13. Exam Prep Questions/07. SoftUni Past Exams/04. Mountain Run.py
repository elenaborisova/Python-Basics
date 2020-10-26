import math
record_secs = float(input())
record_distance_meters = float(input())
secs_per_meter = float(input())

additional_secs = math.floor((record_distance_meters / 50)) * 30
george_total_secs = (secs_per_meter * record_distance_meters) + additional_secs

if george_total_secs < record_secs:
    print(f"Yes! The new record is {george_total_secs:.2f} seconds.")
else:
    print(f"No! He was {george_total_secs - record_secs:.2f} seconds slower.")
