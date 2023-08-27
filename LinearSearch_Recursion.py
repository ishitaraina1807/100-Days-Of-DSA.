def linear_search(arr, size, key):
    
    if (size == 0):
        return -1

    elif (arr[size - 1] == key):
        return size - 1
    
    return linear_search(arr, size - 1, key)

