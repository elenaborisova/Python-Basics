eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for egg in range(1, eggs + 1):
    color = input() # red orange blue or green

    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")

if max(red, orange, blue, green) == red:
    print(f"Max eggs: {red} -> red")
elif max(red, orange, blue, green) == orange:
    print(f"Max eggs: {orange} -> orange")
if max(red, orange, blue, green) == blue:
    print(f"Max eggs: {blue} -> blue")
if max(red, orange, blue, green) == green:
    print(f"Max eggs: {green} -> green")

