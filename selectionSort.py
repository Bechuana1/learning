def findSmallest(arr):
     smallest = arr[0]
     for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

     return smallest




def selectionSort(arr):# Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        return newArr


print(selectionSort([5, 3, 6, 2, 10]))

















#
# def find_smallest(arr):
#     smallest= arr[0]
#     smallest_index = 0
#
#
#     for i in range(0, len(arr)):
#         for j in range(i +1, len(arr)):
#             if arr[i] < arr[j]:
#
#                 arr[i]
#                 smallest = arr[i]
#                 smallestIndex = i
#             return smallest
#
#
# print(find_smallest([3,5,6,5,9,1,67]))

#
# #
# # def selection_sort(arr):
# #
# #     newArr = []
# #
# #     for i in range(len(arr)):
# #         smallest = find_smallest(arr)
# #         newArr.append(arr.pop(smallest))
# #         return newArr
# #
# #

# #
# # #
# def findSmallest(arr):
#     min = arr[0] #Stores the smallest value
#     #smallest_index = 0 #Stores the index of the smallest value
#     for i in range(0, len(arr)):
#         if (arr[i] < min):
#             min = arr[i]
#             #smallest_index = i
#             return min
#
#
#
# arr = [34, 71, 18, 3, 15, 12]
# print(findSmallest(arr))
# # #Now you can use this function to write selection sort:
