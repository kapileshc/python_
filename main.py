from calculator import calculator

from tdsCalculator import tds_calculator

from emploeeDetails import EmployeeDetails

print('hello world ')


# num1 = input('Enter a number1 : ')
# operator = input('Enter a operator +,-,*,/ :')
# num2 = input('Enter a number2 : ')
#
# print(int(calculator(int(num1),int(num2),operator)))

print(tds_calculator(500000,False))

emp = EmployeeDetails('kapil',27,20000,True)


print(emp.get_name())



