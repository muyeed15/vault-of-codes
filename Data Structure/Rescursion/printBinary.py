def printBinary(number):
    if number < 0:
        print("-", end="")
        number *= (-1)

    if number == 0:
        return
    
    printBinary(number//2)
    print(number % 2, end="")


printBinary(-6)
