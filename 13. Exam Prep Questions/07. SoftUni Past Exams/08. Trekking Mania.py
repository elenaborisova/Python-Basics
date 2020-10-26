groups_count = int(input())
musala = 0
montblanc = 0
kilimandzaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(1, groups_count + 1):
    people_per_group = int(input())
    total_people += people_per_group

    if people_per_group <= 5:
        musala += people_per_group
    elif 6 <= people_per_group <= 12:
        montblanc += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimandzaro += people_per_group
    elif 26 <= people_per_group <= 40:
        k2 += people_per_group
    elif people_per_group >= 41:
        everest += people_per_group

print(f"{musala / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimandzaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")

