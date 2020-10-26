trunk_capacity = float(input())
luggage_count = 0

command = input()
while command != "End":
    luggage_volume = float(command)

    if (luggage_count + 1) % 3 == 0:
        luggage_volume += luggage_volume * 0.1

    if trunk_capacity < luggage_volume:
        print(f"No more space!")
        break

    luggage_count += 1
    trunk_capacity -= luggage_volume
    command = input()

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {luggage_count} suitcases loaded.")
