target_height = int(input())
curr_height = target_height - 30
failed_attempts = 0
total_attempts = 0

while True:
    curr_jump = int(input())
    total_attempts += 1

    if curr_jump > curr_height >= target_height:
        print(f"Tihomir succeeded, he jumped over {curr_height}cm after {total_attempts} jumps.")
        break

    if curr_jump > curr_height:
        # successful jump
        curr_height += 5
        failed_attempts = 0
    else:
        # unsuccessful jump
        failed_attempts += 1
        if failed_attempts == 3:
            print(f"Tihomir failed at {curr_height}cm after {total_attempts} jumps.")
            break

