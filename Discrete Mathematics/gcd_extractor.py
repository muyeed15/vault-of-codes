def gcd(number1, number2):
    divisors = []

    maximum = max(number1, number2)
    minimum = min(number1, number2)

    for i in range(1, (minimum + 1)):
        if (minimum % i == 0) and (maximum % i == 0):
            divisors.append(i)
        
    return max(divisors)
