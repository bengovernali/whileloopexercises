i = 0

while i <= 99:
    triangle_num = 0
    j = 0
    while j <= i:
        triangle_num += j
        j += 1
    i += 1
    print(triangle_num)