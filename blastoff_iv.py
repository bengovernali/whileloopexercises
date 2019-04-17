i = int(input("Number to count from? "))

while i > 20:
    print("Sorry, please choose a number lower than 20")
    i = int(input("Number to count from? "))

while i >= 0:
    print(i)
    i -= 1

print("Blastoff!")    