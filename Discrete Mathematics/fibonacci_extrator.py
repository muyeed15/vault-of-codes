def fibonacci(number):
    if 0 <= number <= 1:
        return number
    
    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacciExtractor(start, end):
    fibList = []
    for i in range(start, end+1):
        fibList.append(fibonacci(i))

    return fibList


print(fibonacciExtractor(0, 10))
