budget = float(input())

actor_name = input()
while actor_name != "ACTION":

    if len(actor_name) <= 15:
        wage = float(input())
    else:
        wage = 0.2 * budget

    if budget < wage:
        print(f"We need {wage - budget:.2f} leva for our actors.")
        break

    budget -= wage
    actor_name = input()

if actor_name == "ACTION":
    print(f"We are left with {budget:.2f} leva.")