import math

wall_height = int(input())
wall_width = int(input())
percentage_not_painted = int(input())

wall_area = wall_width * wall_height * 4
area_not_painted = wall_area * (percentage_not_painted / 100)
area_painted = math.ceil(wall_area - area_not_painted)

command = input()
while command != "Tired!":
    paint_liters = int(command)
    area_painted -= paint_liters

    if area_painted < 0:
        print(f"All walls are painted and you have {abs(area_painted)} l paint left!")
        break
    elif area_painted == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break

    command = input()

if command == "Tired!":
    print(f"{area_painted} quadratic m left.")