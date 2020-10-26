food_kg = int(input())
food_grams = food_kg * 1000
total_grams = 0

command = input()
while command != "Adopted":
    grams_per_serving = int(command)
    total_grams += grams_per_serving

    command = input()

if total_grams <= food_grams:
    print(f"Food is enough! Leftovers: {food_grams - total_grams} grams.")
else:
    print(f"Food is not enough. You need {total_grams - food_grams} grams more.")