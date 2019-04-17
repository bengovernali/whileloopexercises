user_input = "yes"
coin_count = 0

print("You have 0 coins")

while user_input == "yes":
    coin_count += 1
    user_input = input("Do you want another coin? ")
    if user_input == "yes":
        print(("You have %d coins.") % coin_count)
    elif user_input == "no":
        print("Bye")    