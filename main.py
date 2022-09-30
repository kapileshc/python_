from calculator import calculator

print('hello world ')


num1 = input('Enter a number1 : ')
operator = input('Enter a operator +,-,*,/ :')
num2 = input('Enter a number2 : ')

print(int(calculator(int(num1),int(num2),operator)))

