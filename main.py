 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print('heello world ')

def calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return abs(num1-num2)
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return max(num1,num2)/min(num1,num2)
    else:
        return "select a correct operator"

num1 = input('Enter a number1 : ')
operator = input('Enter a operator +,-,*,/ :')
num2 = input('Enter a number2 : ')

print(calculator(int(num1),int(num2),operator))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
