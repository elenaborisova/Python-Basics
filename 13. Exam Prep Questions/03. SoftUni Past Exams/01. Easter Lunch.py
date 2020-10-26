bread_count = int(input())
egg_baskets_count = int(input())
cookies_kg = int(input())

bread_price = bread_count * 3.20
egg_baskets_price = egg_baskets_count * 4.35
eggs_count = egg_baskets_count * 12
eggs_paint_price = eggs_count * 0.15
cookies_price = cookies_kg * 5.40

expenses = bread_price + egg_baskets_price + eggs_paint_price + cookies_price
print(f"{expenses:.2f}")