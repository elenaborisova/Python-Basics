initial_eggs_count = int(input())
sold_eggs = 0

command = input() # buy or fill
while command != "Close":
    bought_or_filled_count = int(input())

    if command == "Buy" and bought_or_filled_count > initial_eggs_count:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {initial_eggs_count}.")
        break

    if command == "Buy":
        sold_eggs += bought_or_filled_count
        initial_eggs_count -= bought_or_filled_count
    elif command == "Fill":
        initial_eggs_count += bought_or_filled_count

    command = input()  # buy or fill

if command == "Close":
    print(f"Store is closed!")
    print(f"{sold_eggs} eggs sold.")