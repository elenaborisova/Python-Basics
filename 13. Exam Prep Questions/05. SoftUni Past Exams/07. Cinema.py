cinema_capacity = int(input())
ticket_price = 5
profit = 0

command = input()
while command != "Movie time!":
    people_count = int(command)

    if people_count > cinema_capacity:
        print(f"The cinema is full.")
        break

    cinema_capacity -= people_count
    ticket_price *= people_count

    if people_count % 3 == 0:
        ticket_price -= 5

    profit += ticket_price
    ticket_price = 5
    command = input()

if command == "Movie time!":
    print(f"There are {cinema_capacity} seats left in the cinema.")

print(f"Cinema income - {profit} lv.")