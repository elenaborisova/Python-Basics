import sys

movies = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
total_rating = 0
winner_name = ""
loser_name = ""

for movie in range(movies):
    movie_name = input()
    rating = float(input())
    total_rating += rating

    if rating > highest_rating:
        highest_rating = rating
        winner_name = movie_name

    elif rating < lowest_rating:
        lowest_rating = rating
        loser_name = movie_name

print(f"{winner_name} is with highest rating: {highest_rating:.1f}")
print(f"{loser_name} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {total_rating / movies:.1f}")