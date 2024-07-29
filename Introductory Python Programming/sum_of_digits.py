def digitSum(number):
    total = 0
    while number != 0:
        total += (number % 10)
        number = number // 10

    return total

print(digitSum(1323))