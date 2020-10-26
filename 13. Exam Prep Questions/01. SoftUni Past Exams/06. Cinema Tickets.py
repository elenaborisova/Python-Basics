student = 0
standard = 0
kid = 0
total_tickets = 0
taken_seats = 0

movie_name = input()
while movie_name != "Finish":
    available_seats = int(input())

    ticket_type = input()
    while ticket_type != "End":

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1

        total_tickets += 1
        taken_seats += 1

        if taken_seats == available_seats:
            break

        ticket_type = input()

    print(f"{movie_name} - {taken_seats / available_seats * 100:.2f}% full.")
    taken_seats = 0
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")
