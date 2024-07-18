def interpolationSearch(data, target):
    low = 0
    high = len(data) - 1

    while (low <= high) and (target >= data[low]) and (target <= data[high]):
        if low == high:
            if data[low] == target:
                return low
            return False

        position = low + ((target - data[low]) * (high - low) // (data[high] - data[low]))

        if data[position] == target:
            return position
        elif data[position] < target:
            low = position + 1
        else:
            high = position - 1

    return False


print(interpolationSearch([1, 3, 5, 14, 21, 25, 26, 27], 25))