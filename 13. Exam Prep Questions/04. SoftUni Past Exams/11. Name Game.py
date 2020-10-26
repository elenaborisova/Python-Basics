points = 0
highest_score = 0
winner_name = ""

player_name = input()
while player_name != "Stop":

    for char in range(len(player_name)):
        num = int(input())

        if num == ord(player_name[char]):
            points += 10
        else:
            points += 2

        if points >= highest_score:
            highest_score = points
            winner_name = player_name

    points = 0
    player_name = input()

print(f"The winner is {winner_name} with {highest_score} points!")