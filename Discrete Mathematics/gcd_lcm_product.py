def gcd(number1, number2):
    divisors = []

    maximum = max(number1, number2)
    minimum = min(number1, number2)

    for i in range(1, (minimum + 1)):
        if (minimum % i == 0) and (maximum % i == 0):
            divisors.append(i)
        
    return max(divisors)


def lcm(number1, number2):
    maximum = max(number1, number2)

    while True:
        if (maximum %  number1 == 0) and (maximum % number2 == 0):
            return maximum
        maximum += 1


def gcd_lcm_product_theorem(number1, number2):
    product = (number1 * number2)
    gcd_value = gcd(number1, number2)
    lcm_value = lcm(number1, number2)
    gcd_lcm_product = (gcd_value * lcm_value)

    if product == gcd_lcm_product:
        statement = True
    else:
        statement = False

    print(f"Product: {number1}x{number2} = {product}\
          \nGCD LCM Product: {gcd_value}x{lcm_value} = {gcd_lcm_product}\
          \nTheorem: {statement}")


gcd_lcm_product_theorem(120, 500)
