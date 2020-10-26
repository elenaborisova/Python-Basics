curr_points = 0
max_points = 0
movie_count = 0
winning_movie = ""

movie_name = input()
while movie_name != "STOP":
    movie_count += 1

    for char in movie_name:
        curr_points += ord(char)

        if char.islower():
            curr_points -= 2 * len(movie_name)
        elif char.isupper():
            curr_points -= len(movie_name)

        if curr_points > max_points:
            max_points = curr_points
            winning_movie = movie_name

    curr_points = 0

    if movie_count == 7:
        print(f"The limit is reached.")
        break

    movie_name = input()

print(f"The best movie for you is {winning_movie} with {max_points} ASCII sum.")