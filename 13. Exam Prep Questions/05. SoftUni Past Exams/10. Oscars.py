actor_name = input()
academy_initial_points = float(input())
judges_count = int(input())

for judge in range(1, judges_count + 1):
    judge_name = input()
    judge_points = float(input())

    actor_points_received = len(judge_name) * judge_points / 2
    academy_initial_points += actor_points_received

    if academy_initial_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_initial_points:.1f}!")
        break

if academy_initial_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_initial_points:.1f} more!")