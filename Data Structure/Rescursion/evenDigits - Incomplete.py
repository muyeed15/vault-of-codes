def evenDigits(number, flag = False):
    if number == 0:
        return 0
    
    print(number)
    return evenDigits(number//10) + (number % 10) * (10**len(str(number)))

print(evenDigits(8342116))
