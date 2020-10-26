destination = input() # Bansko Borovets Varna or Burgas
deal_type = input()
vip = input()
days = int(input())
price = 0
destinations = ["Bansko", "Borovets", "Varna", "Burgas"]
deal_types = ["withEquipment", "noEquipment", "withBreakfast", "noBreakfast"]

if days < 1:
    print(f"Days must be positive number!")
    quit()

if destination not in destinations or deal_type not in deal_types:
    print("Invalid input!")
    quit()

if destination == "Bansko" or destination == "Borovets":

    if deal_type == "withEquipment":

        if days > 7:
            price = 100 * (days - 1)
        else:
            price = 100 * days

        if vip == "yes":
            price -= price * 0.1

    elif deal_type == "noEquipment":

        if days > 7:
            price = 80 * (days - 1)
        else:
            price = 80 * days

        if vip == "yes":
            price -= price * 0.05

elif destination == "Varna" or destination == "Burgas":

    if deal_type == "withBreakfast":

        if days > 7:
            price = 130 * (days - 1)
        else:
            price = 130 * days

        if vip == "yes":
            price -= price * 0.12

    elif deal_type == "noBreakfast":

        if days > 7:
            price = 100 * (days - 1)
        else:
            price = 100 * days

        if vip == "yes":
            price -= price * 0.07

print(f"The price is {price:.2f}lv! Have a nice time!")