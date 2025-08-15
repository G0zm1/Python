print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
prize = 0

if size == "S":
    prize += 15
elif size == "M":
    prize += 20
elif size == "L":
    prize += 25
else:
    print("You have to choose S, M or L! ")

if pepperoni == "Y":
    if size == "S":
        prize += 2
    else:
        prize += 3

if extra_cheese == "Y":
    prize += 1


print(f"Your final bill is: ${prize}.")
