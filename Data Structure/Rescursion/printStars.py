def printStars(number):
    if number == 0:
        return
    
    printStars(number - 1)
    
    print("*" * number)

printStars(5)
