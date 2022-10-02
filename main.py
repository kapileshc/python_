from calculator import calculator

from tdsCalculator import tds_calculator

from emploeeDetails import EmployeeDetails

from students import Students,Course

from bigO import cal_bigO, cal_while_bigO

import dict

import wordGuessGame

print('hello world ')


# num1 = input('Enter a number1 : ')
# operator = input('Enter a operator +,-,*,/ :')
# num2 = input('Enter a number2 : ')
#
# print(int(calculator(int(num1),int(num2),operator)))

print(tds_calculator(500000,False))

emp = EmployeeDetails('kapil',27,20000,True)

student1 = Students('kapilesh',27,'A')

cos = Course('python')
cos.add_students(student1)

print(cos.get_students()[0].age)

cal_bigO()

cal_while_bigO()


print(dict.profile_details)
print(dict.profile_details.get('firstname','name not available'))

print(emp.get_name())

wordGuessGame



