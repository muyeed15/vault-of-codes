def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                maximum = array[i]
                minimum = array[j]
                array[i] = minimum
                array[j] = maximum

    return array


print(bubbleSort([8, 1, 5, 3, 0, 6, 9, 2, 4, 7]))
