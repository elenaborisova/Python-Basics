guest_count = int(input())
package_price_per_person = float(input())
budget = float(input())

if 10 <= guest_count <= 15:
    package_price_per_person -= package_price_per_person * 0.15
elif 15 < guest_count <= 20:
    package_price_per_person -= package_price_per_person * 0.2
elif guest_count > 20:
    package_price_per_person -= package_price_per_person * 0.25

total_package_price = package_price_per_person * guest_count
cake_price = budget * 0.1

total_expenses = total_package_price + cake_price

if budget >= total_expenses:
    print(f"It is party time! {budget - total_expenses:.2f} leva left.")
else:
    print(f"No party! {total_expenses - budget:.2f} leva needed.")
