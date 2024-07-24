def lcm(number1, number2):
    maximum = max(number1, number2)

    while True:
        if (maximum %  number1 == 0) and (maximum % number2 == 0):
            return maximum
        maximum += 1
