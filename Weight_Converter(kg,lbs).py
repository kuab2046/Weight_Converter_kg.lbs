kind_of_change = int(input("would you like to convert (kg to lbs) / (lbs to kg), ( 1 / 2 ): "))

kg_to_lbs = 2.20462262
lbs_to_kg = 0.45359237

if kind_of_change not in [ 1 , 2]:
    print("chose the right kind of operation")
    exit(0)

if kind_of_change == 1:
    amount = input("how many kilograms would you like to convert into pounds?: ")
    try:
        amount = float(amount)
    except ValueError:
        print("you haven't entered a number")
        exit(0)
    if amount < 0:
        print("it is impossible for mass to be negative")
        exit(0)
    result = amount * kg_to_lbs
    print(f"after converting {amount} kg to pounds your result is {round(result, 2)} lbs")
elif kind_of_change == 2:
    amount = input("how many lbs would you like to convert into kilograms?: ")
    try:
        amount = float(amount)
    except ValueError:
        print("you haven't entered a number")
        exit(0)
    if amount < 0:
        print("it is impossible for mass to be negative")
        exit(0)
    result = amount * lbs_to_kg
    print(f"after converting {amount} pounds to kg your result is {round(result, 2)} kg")