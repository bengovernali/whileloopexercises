width  = int(input("Width? "))
height = int(input("Height? "))

i = 0

while i <= height - 1:
    if (i == 0) or (i == height - 1):
        print("*" * width)
    else:
        print("*" + (" " * (width - 2)) + "*") 
    i += 1 