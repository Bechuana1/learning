# def recurse(num):
#     if num < 2:
#         return num
#     else:
#         return num * recurse(num -1)

# print(recurse(num))


def factorial(num):
    sum = 1

    for i in range(1, num + 1):
        sum = sum *i

    print("the factorial of ", num, " is ",sum)

num = int(input("enter a number to find factorial"))
print(factorial(num))




