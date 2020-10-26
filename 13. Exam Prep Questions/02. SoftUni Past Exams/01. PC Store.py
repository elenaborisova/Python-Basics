processor_price_dollars = float(input())
video_card_price_dollars = float(input())
ram_memory_price_dollars = float(input())
ram_memory_count = int(input())
discount_percentage = float(input())

processor_price_leva = processor_price_dollars * 1.57
processor_price_leva -= processor_price_leva * discount_percentage

video_card_price_leva = video_card_price_dollars * 1.57
video_card_price_leva -= video_card_price_leva * discount_percentage

ram_memory_price_leva = ram_memory_price_dollars * 1.57
ram_memory_price_leva *= ram_memory_count

total = processor_price_leva + video_card_price_leva + ram_memory_price_leva
print(f"Money needed - {total:.2f} leva.")