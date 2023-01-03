def binary(arr, item):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if item > arr[mid]:
            low = mid +1

        elif item < arr[mid]:
            high = mid - 1

        else:
            return mid
    return -1




arr = [2,4,6,8,9]
item = 6
result = binary(arr,item)
print(result, "and searched item is ", arr[result])