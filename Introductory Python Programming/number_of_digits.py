def digitNumber(number):
    count = 0
    while number != 0:
        count += 1
        number = number // 10

    return count

print(digitNumber(1323))