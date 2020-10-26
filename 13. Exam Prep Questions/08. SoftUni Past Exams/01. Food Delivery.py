chicken_menu_count = int(input())
fish_menu_count = int(input())
vegiterian_menu_count = int(input())

chicken_menu_price = chicken_menu_count * 10.35
fish_menu_price = fish_menu_count * 12.40
vegiterian_menu_price = vegiterian_menu_count * 8.15

total_menu_price = chicken_menu_price + fish_menu_price + vegiterian_menu_price
desert_price = total_menu_price * 0.2
delivery_price = 2.50

total_sum = total_menu_price + desert_price + delivery_price
print(f"Total: {total_sum:.2f}")