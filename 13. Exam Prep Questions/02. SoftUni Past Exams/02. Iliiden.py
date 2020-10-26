people_count = int(input())
strength_per_person = int(input())
ilidan_blood = int(input())

total_strength = people_count * strength_per_person

if total_strength < ilidan_blood:
    print(f"You are not prepared! You need {abs(ilidan_blood - total_strength)} more points.")
else:
    print(f"Illidan has been slain! You defeated him with {abs(total_strength - ilidan_blood)} points.")