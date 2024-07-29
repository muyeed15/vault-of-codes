def minimax(array):
    minV = array[0]
    maxV = array[0]
    for i in range(len(array)):
        if array[i] < minV:
            minV = array[i]
        
        if array[i] > maxV:
            maxV = array[i]

    return minV, maxV


print(minimax([8, 1, 5, 3, 0, 6, 9, 2, 4, 7]))
