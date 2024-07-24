def powerSum(number):
    total = 0
    for i in range(1, number+1):
        total += i**i
    
    return total


print(powerSum(5))
