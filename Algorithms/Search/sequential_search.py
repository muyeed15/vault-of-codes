def sequentialSearch(data, terget):
    i = 0
    while i < len(data):
        if (terget == data[i]):
            return i
        
        i += 1
    
    return False


print(sequentialSearch([6, 9, 3, 2, 5], 2))
