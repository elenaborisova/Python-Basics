voucher_value = int(input())
ticket_count = 0
other_purchases = 0

purchase = input()
while purchase != "End":

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher_value:
            break
        ticket_count += 1
    else:
        price = ord(purchase[0])
        if price > voucher_value:
            break
        other_purchases += 1

    voucher_value -= price

    purchase = input()

print(f"{ticket_count}")
print(f"{other_purchases}")