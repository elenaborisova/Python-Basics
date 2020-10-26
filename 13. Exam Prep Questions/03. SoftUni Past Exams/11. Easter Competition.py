bread_count = int(input())
total_grade = 0
max_grade = 0
winner_chef = ""

for bread in range(1, bread_count + 1):
    chef_name = input()

    while True:
        grade = input()

        if grade == "Stop":
            print(f"{chef_name} has {total_grade} points.")
            if chef_name == winner_chef:
                print(f"{chef_name} is the new number 1!")
            break

        grade = int(grade)
        total_grade += grade

        if total_grade > max_grade:
            max_grade = total_grade
            winner_chef = chef_name

    total_grade = 0

print(f"{winner_chef} won competition with {max_grade} points!")