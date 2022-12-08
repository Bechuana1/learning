arr = [3,5,6,5,9,1,67]

min = arr[0]


for i in range(0, len(arr)):
    if arr[i] < min:
        min = arr[i]


print(min)
