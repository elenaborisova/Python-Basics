bitcoins = int(input())
chinese_yuans = float(input())
commision = float(input())

bitcoins_to_leva = bitcoins * 1168
leva_to_euro = bitcoins_to_leva / 1.95

chinese_yuans_to_dolars = chinese_yuans * 0.15
dolars_to_leva = chinese_yuans_to_dolars * 1.76
leva_to_euro_two = dolars_to_leva / 1.95

final_sum_euro = leva_to_euro + leva_to_euro_two
final_sum_euro -= final_sum_euro * (commision / 100)

print(f"{final_sum_euro:.2f}")

