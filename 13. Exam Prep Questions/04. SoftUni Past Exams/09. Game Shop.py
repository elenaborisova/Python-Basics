hearthstone = 0
fornite = 0
overwatch = 0
others = 0

sold_games = int(input())
for sold_game in range(1, sold_games + 1):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

all_games = hearthstone + fornite + overwatch + others

print(f"Hearthstone - {hearthstone / all_games * 100:.2f}%")
print(f"Fornite - {fornite / all_games * 100:.2f}%")
print(f"Overwatch - {overwatch / all_games * 100:.2f}%")
print(f"Others - {others / all_games * 100:.2f}%")