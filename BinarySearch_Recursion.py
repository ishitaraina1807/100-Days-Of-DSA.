def binarySearch(arr, left, right, number):
    
    if left > right:
        return -1
        mid = (left + right) // 2 
    if number == arr[mid]:
        return mid
    elif number < arr[mid]:
        return binarySearch(arr, left, mid - 1, number)
    else:
        return binarySearch(arr, mid + 1, right, number) 
