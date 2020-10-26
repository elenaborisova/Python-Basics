customers = int(input())
item_count = 0
final_price = 0
total_price_all_customers = 0

for customer in range(1, customers + 1):

    while True:
        item = input()

        if item == "Finish":

            if item_count % 2 == 0:
                final_price -= final_price * 0.2

            total_price_all_customers += final_price
            print(f"You purchased {item_count} items for {final_price:.2f} leva.")
            break

        if item == "basket":
            final_price += 1.50
        elif item == "wreath":
            final_price += 3.80
        elif item == "chocolate bunny":
            final_price += 7

        item_count += 1

    final_price = 0
    item_count = 0

print(f"Average bill per client is: {total_price_all_customers / customers:.2f} leva.")