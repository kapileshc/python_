from calculator import calculator

from tdsCalculator import tds_calculator

from emploeeDetails import EmployeeDetails

from students import Students,Course

from bigO import cal_bigO, cal_while_bigO

import dict

import useful_tools

from Requirements import Requirements

from paymentDetails import paymentDetails


import filehandling

import wordGuessGame

import error

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

# print(cos.get_students()[0].age)

cal_bigO()

cal_while_bigO()


# print(dict.profile_details)
# print(dict.profile_details.get('firstname','name not available'))
#
# print(emp.get_name())

# wordGuessGame
#
# error
#
# filehandling

print(useful_tools.get_file_extension('index.html'))

print(useful_tools.roll_dice(100))


requirement1 = Requirements('HRM','2 hr', 5000, 2, 'python')

print(requirement1.manpower_required)
print(requirement1.project_name)
print(requirement1.cost_estimate)

emp1 = paymentDetails()
print(emp1.generate_payslip())