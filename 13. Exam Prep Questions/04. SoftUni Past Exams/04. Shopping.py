budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_cards_price = video_cards_count * 250
processors_price = (0.35 * video_cards_price) * processors_count
ram_memory_price = (0.1 * video_cards_price) * ram_memory_count

final_price = video_cards_price + processors_price + ram_memory_price

if video_cards_count > processors_count:
    final_price -= final_price * 0.15

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")
