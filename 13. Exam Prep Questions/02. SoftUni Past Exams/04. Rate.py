initial_deposit_sum = float(input())
months = int(input())
flat_tax = initial_deposit_sum
progressive_tax = 0
curr_month = initial_deposit_sum

for month in range(1, months + 1):
    flat_tax += initial_deposit_sum * 0.03

for month in range(1, months + 1):
    progressive_tax = curr_month + curr_month * 0.027
    curr_month = progressive_tax

print(f"Simple interest rate: {flat_tax:.2f} lv.")
print(f"Complex interest rate: {progressive_tax:.2f} lv.")

if min(flat_tax, progressive_tax) == flat_tax:
    print(f"Choose a complex interest rate. You will win {abs(progressive_tax - flat_tax):.2f} lv.")
else:
    print(f"Choose a simple interest rate. You will win {abs(progressive_tax - flat_tax):.2f} lv.")

