height = int(input("Height? "))

i = 0

while i <= height - 1:
    print((" " * ((height-1) - i)) + ("*" + ("*" * (i * 2))))  
    i += 1