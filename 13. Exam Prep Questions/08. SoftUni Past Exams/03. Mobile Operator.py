contract_duration = input() # one or two years
contract_type = input() # small middle large or extralarge
mobile_data_added = input() # yes or no
number_of_months = int(input())
contract_price = 0

if contract_duration == "one":

    if contract_type == "Small":
        contract_price = 9.98
    elif contract_type == "Middle":
        contract_price = 18.99
    elif contract_type == "Large":
        contract_price = 25.98
    elif contract_type == "ExtraLarge":
        contract_price = 35.99

elif contract_duration == "two":

    if contract_type == "Small":
        contract_price = 8.58
    elif contract_type == "Middle":
        contract_price = 17.09
    elif contract_type == "Large":
        contract_price = 23.59
    elif contract_type == "ExtraLarge":
        contract_price = 31.79

if mobile_data_added == "yes":
    if contract_price <= 10:
        contract_price += 5.50
    elif contract_price <= 30:
        contract_price += 4.35
    elif contract_price > 30:
        contract_price += 3.85

if contract_duration == "two":
    contract_price -= contract_price * 0.0375

print(f"{contract_price * number_of_months:.2f} lv.")