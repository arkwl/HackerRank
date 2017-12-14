def nth(n):

    digit = 1
    pow = 1
    while 1:
        if (n - pow * 9 * digit > 0):
            n = n - pow * 9 * digit
            digit = digit + 1
            pow = pow * 10
        else:
            break

    if (pow == 1)
    number = pow + n // digit
    index = n % digit
    print(number)
    print(index)

nth(9)
print()
nth(10)
print()
nth(11)
print()
nth(130)
print()
nth(250)
