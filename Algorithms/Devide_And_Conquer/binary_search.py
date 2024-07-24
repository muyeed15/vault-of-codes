def binarySearch(array, first, last, terget):
    if last >= first:
        middle = int((last + first)/2)
    else:
        return False
    
    if array[middle] == terget:
        return middle
    
    elif array[middle] < terget:
        return binarySearch(array, (middle + 1), last, terget)
    
    elif array[middle] > terget:
        return binarySearch(array, first, (middle - 1), terget)


print(binarySearch([1, 2, 3, 3, 4, 5, 7, 9], 0, 7, 7))
