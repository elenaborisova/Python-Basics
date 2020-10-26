team_name = input()
games = int(input())
wins = 0
loses = 0
ties = 0
all_games = 0
points = 0

if games == 0:
    print(f"{team_name} hasn't played any games during this season.")
    quit()

for game in range(1, games + 1):
    result = input() # W or D or L
    all_games += 1

    if result == "W":
        wins += 1
        points += 3
    elif result == "D":
        ties += 1
        points += 1
    elif result == "L":
        loses += 1

print(f"{team_name} has won {points} points during this season.")
print(f"Total stats:")
print(f"## W: {wins}")
print(f"## D: {ties}")
print(f"## L: {loses}")
print(f"Win rate: {wins / all_games * 100:.2f}%")