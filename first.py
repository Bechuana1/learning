"""def binary_search(arr, low, high, item):
    #low = 0
   # high = len(list) - 1

    while low <= high:
        mid = len(list)//2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid + 1
        else:
            low = mid + 1

    return none
"""

def search(arr, low , high, item):
    if high >= low:
        mid = (high + low)//2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return search(arr,low,mid- 1,item)

        else:
            return search(arr,mid+1,high, item)

    else:
        return -1

arr = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
item = 6

result = search(arr, 0, len(arr) - 1, item)
if result != -1:
    print("element is present at index", str(result))

else:
    print("element not present")


