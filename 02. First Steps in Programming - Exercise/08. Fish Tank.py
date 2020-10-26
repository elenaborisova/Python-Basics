length = int(input())
width = int(input())
height = int(input())
used_volume_percentage = float(input())

# 1 liter = 1 dm^3
# 1 liter = 10 cm^3
# 1 cm^3 = 0.001 liters

volume_liters = (length * width * height) * 0.001

total_water_volume_liters = volume_liters - volume_liters*(used_volume_percentage/100)
print(total_water_volume_liters)
