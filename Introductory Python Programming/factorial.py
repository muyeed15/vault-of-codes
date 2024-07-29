def factorial(number):
    fac = 1
    while number > 1:
        fac *= number
        number -= 1

    return fac


print(factorial(5))
