movie_name = input()
cinema_type = input()
tickets_purchased = int(input())
price = 0

if movie_name == "A Star Is Born":
    if cinema_type == "normal":
        price = tickets_purchased * 7.50
    elif cinema_type == "luxury":
        price = tickets_purchased * 10.50
    elif cinema_type == "ultra luxury":
        price = tickets_purchased * 13.50
elif movie_name == "Bohemian Rhapsody":
    if cinema_type == "normal":
        price = tickets_purchased * 7.35
    elif cinema_type == "luxury":
        price = tickets_purchased * 9.45
    elif cinema_type == "ultra luxury":
        price = tickets_purchased * 12.75
elif movie_name == "Green Book":
    if cinema_type == "normal":
        price = tickets_purchased * 8.15
    elif cinema_type == "luxury":
        price = tickets_purchased * 10.25
    elif cinema_type == "ultra luxury":
        price = tickets_purchased * 13.25
elif movie_name == "The Favourite":
    if cinema_type == "normal":
        price = tickets_purchased * 8.75
    elif cinema_type == "luxury":
        price = tickets_purchased * 11.55
    elif cinema_type == "ultra luxury":
        price = tickets_purchased * 13.95

print(f"{movie_name} -> {price:.2f} lv.")