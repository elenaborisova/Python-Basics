import math

days = int(input())
total_food_amount = float(input())

total_dog_food_eaten = 0
total_cat_food_eaten = 0
total_food_eaten_both = 0
biscuits = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    total_dog_food_eaten += dog_food_eaten
    total_cat_food_eaten += cat_food_eaten
    total_food_eaten_both += dog_food_eaten
    total_food_eaten_both += cat_food_eaten

    if day % 3 == 0:
        curr_biscuits = (dog_food_eaten + cat_food_eaten) * 0.1
        biscuits += curr_biscuits


print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten_both / total_food_amount * 100:.2f}% of the food has been eaten.")
print(f"{total_dog_food_eaten / total_food_eaten_both * 100:.2f}% eaten from the dog.")
print(f"{total_cat_food_eaten / total_food_eaten_both * 100:.2f}% eaten from the cat.")
