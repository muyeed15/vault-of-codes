import math

def isPrime(number):
    if number < 2:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True

def primeExtractor(start, end):
    prime = []
    for i in range(start, end+1):
        if isPrime(i) is True:
            prime.append(i)
    
    return prime


print(primeExtractor(1, 100))
