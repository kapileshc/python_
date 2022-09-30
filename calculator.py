
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
