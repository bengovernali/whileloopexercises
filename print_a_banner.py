text = input("Text? ")

i = 0

while i <= 2:
    if i != 1:
        print("*" * (len(text) + 4))
    else:
        print("* " + text + " *") 
    i += 1       