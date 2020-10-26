n = int(input())
remainder_2_count = 0
remainder_3_count = 0
remainder_4_count = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        remainder_2_count += 1
    if num % 3 == 0:
        remainder_3_count += 1
    if num % 4 == 0:
        remainder_4_count += 1

p1 = remainder_2_count / n * 100
p2 = remainder_3_count / n * 100
p3 = remainder_4_count / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
