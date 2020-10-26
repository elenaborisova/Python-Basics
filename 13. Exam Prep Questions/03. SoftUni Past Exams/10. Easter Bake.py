import math
bread_count = int(input())
total_sugar_gr = 0
total_flour_gr = 0
max_used_sugar = 0
max_used_flour = 0

for bread in range(1, bread_count + 1):
    sugar_gr = int(input())
    flour_gr = int(input())
    total_sugar_gr += sugar_gr
    total_flour_gr += flour_gr

    if sugar_gr > max_used_sugar:
        max_used_sugar = sugar_gr

    if flour_gr > max_used_flour:
        max_used_flour = flour_gr

sugar_packets = math.ceil(total_sugar_gr / 950)
flour_packets = math.ceil(total_flour_gr / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")
