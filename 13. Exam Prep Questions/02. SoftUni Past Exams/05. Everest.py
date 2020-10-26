days = 1
curr_height = 5364
target_height = 8848

yes_or_no = input()
while yes_or_no != "END":

    meters_walked = int(input())

    if yes_or_no == "Yes":
        days += 1

    if days > 5:
        break

    curr_height += meters_walked

    if curr_height >= target_height:
        break

    yes_or_no = input()

if curr_height >= target_height:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!")
    print(f"{curr_height}")