flour_per_kg_price = float(input())
flour_kgs = float(input())
sugar_kgs = float(input())
egg_baskets_count = int(input())
soy_packets_count = int(input())

total_flour_price = flour_per_kg_price * flour_kgs
sugar_per_kg_price = flour_per_kg_price - flour_per_kg_price * 0.25
total_sugar_price = sugar_per_kg_price * sugar_kgs
egg_baskets_price = flour_per_kg_price + flour_per_kg_price * 0.1
total_egg_baskets_price = egg_baskets_price * egg_baskets_count
soy_packets_price = sugar_per_kg_price - sugar_per_kg_price * 0.8
total_soy_packets_price = soy_packets_price * soy_packets_count

total_expenses = total_flour_price + total_sugar_price + total_egg_baskets_price + total_soy_packets_price
print(f"{total_expenses:.2f}")