"""this program works as a calculator"""
while True:
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))
    action = str(input("Choose action: Add(a), Subt(s), Mult(m), Div(d) ->"))

    def multiply(num1, num2):
        result = num1 * num2
        return result

    def substract(num1, num2):
        result = num1 - num2
        return result


    def divide(num1, num2):
        result = num1 // num2
        return result


    def addition(num1, num2):
        result = num1 + num2
        return result


    if action == "a":
        print(addition(num1, num2))

    elif action == "s":
        print(substract(num1, num2))

    elif action == "m":
        print(multiply(num1, num2))
    else:
        print(divide(num1, num2))






