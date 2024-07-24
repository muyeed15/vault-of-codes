def squareSum(number):
    total = 0
    for i in range(1, number+1):
        total += i**2
    
    return total


print(squareSum(5))
