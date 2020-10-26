rent = int(input())

oscars = rent - rent * 0.3
catering = oscars - oscars * 0.15
sounds = 1/2 * catering

total_expenses = rent + oscars + catering + sounds
print(f"{total_expenses:.2f}")