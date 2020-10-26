movie_name = input() # John Wick, Star Wars or Jumanji
movie_package = input() # Drink, Popcorn or Menu
ticket_count = int(input())
ticket_price = 0

if movie_name == "John Wick":
    if movie_package == "Drink":
        ticket_price = 12 * ticket_count
    elif movie_package == "Popcorn":
        ticket_price = 15 * ticket_count
    elif movie_package == "Menu":
        ticket_price = 19 * ticket_count
elif movie_name == "Star Wars":
    if movie_package == "Drink":
        ticket_price = 18 * ticket_count
    elif movie_package == "Popcorn":
        ticket_price = 25 * ticket_count
    elif movie_package == "Menu":
        ticket_price = 30 * ticket_count
elif movie_name == "Jumanji":
    if movie_package == "Drink":
        ticket_price = 9 * ticket_count
    elif movie_package == "Popcorn":
        ticket_price = 11 * ticket_count
    elif movie_package == "Menu":
        ticket_price = 14 * ticket_count

if movie_name == "Star Wars" and ticket_count >= 4:
    ticket_price -= ticket_price * 0.3
elif movie_name == "Jumanji" and ticket_count == 2:
    ticket_price -= ticket_price * 0.15

print(f"Your bill is {ticket_price:.2f} leva.")