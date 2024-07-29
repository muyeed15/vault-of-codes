def digitNumber(number):
    count = 0
    while number != 0:
        count += 1
        number = number // 10

    return count


def digitReverse(number):
    total = 0
    count = digitNumber(number)
    while number != 0:
        count -= 1
        total += ((number % 10)*10**count)
        number = number // 10

    return total

print(digitReverse(1323))