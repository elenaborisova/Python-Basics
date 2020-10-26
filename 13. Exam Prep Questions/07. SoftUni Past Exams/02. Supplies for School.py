pens_count = int(input())
markers_count = int(input())
liter_cleaner = float(input())
discount_percentage = int(input())

pens_price = pens_count * 5.80
markers_price = markers_count * 7.20
cleaner_price = liter_cleaner * 1.20

total_sum = pens_price + markers_price + cleaner_price
total_sum -= total_sum * (discount_percentage / 100)
print(f"{total_sum:.3f}")