paper_amount_needed_sq_m = int(input())
paint_amount_needed_liters = int(input())
water_amount_needed_liters = int(input())
labor_hours_needed = int(input())

paint_amount_needed_liters += paint_amount_needed_liters * 0.1
paint_price = paint_amount_needed_liters * 14.50

paper_amount_needed_sq_m += 2
paper_price = paper_amount_needed_sq_m * 1.50

water_price = water_amount_needed_liters * 5

materials_total_price = paper_price + paint_price + water_price + 0.40
labor_price = (0.3 * materials_total_price) * labor_hours_needed

total_expenses = materials_total_price + labor_price
print(f"Total expenses: {total_expenses:.2f} lv.")
