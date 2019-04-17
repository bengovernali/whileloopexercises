number = int(input("Please enter a number: "))
i = number

print("Factors of %d: " % number)



while i > 0:
    if number % i == 0:
        factor1 = number / i
        if factor1 < i:
            print("%d and %d" % (i, factor1))
    i -= 1    