movie_name = input()
days = int(input())
ticket_count = int(input())
ticket_price = float(input())
profit_percentage = int(input())

ticket_profit = ticket_count * ticket_price * days
cinema_profit = ticket_profit * (profit_percentage / 100)
studio_profit = ticket_profit - cinema_profit

print(f"The profit from the movie {movie_name} is {studio_profit:.2f}lv.")