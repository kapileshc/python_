from calculator import calculator
#
# from tdsCalculator import tds_calculator
#
# from emploeeDetails import EmployeeDetails
#
# from students import Students,Course
#
# from bigO import cal_bigO, cal_while_bigO
#
# import dict
#
# import useful_tools
#
# from Requirements import Requirements
#
# from paymentDetails import paymentDetails
#
# from emailslicer import email_silcer
#
# import filehandling
#
# import wordGuessGame
#
# import error
#
# print('hello world ')
#
#
# # num1 = input('Enter a number1 : ')
# # operator = input('Enter a operator +,-,*,/ :')
# # num2 = input('Enter a number2 : ')
# #
# # print(int(calculator(int(num1),int(num2),operator)))
#
# print(tds_calculator(500000,False))
#
# emp = EmployeeDetails('kapil',27,20000,True)
#
# student1 = Students('kapilesh',27,'A')
#
# cos = Course('python')
# cos.add_students(student1)
#
# # print(cos.get_students()[0].age)
#
# cal_bigO()
#
# cal_while_bigO()
#
#
# [user,email] = (email_silcer('kapilesh1@gmail.com'))
#
# print('Name : ' ,user, 'Email : ', email)
# # print(dict.profile_details)
# # print(dict.profile_details.get('firstname','name not available'))
# #
# # print(emp.get_name())
#
# # wordGuessGame
# #
# # error
# #
# # filehandling
#
# print(useful_tools.get_file_extension('index.html'))
#
# print(useful_tools.roll_dice(100))
#
#
# requirement1 = Requirements('HRM','2 hr', 5000, 2, 'python')
#
# print(requirement1.manpower_required)
# print(requirement1.project_name)
# print(requirement1.cost_estimate)
#
# emp1 = paymentDetails()
# print(emp1.get_passport_details())
# import mystriousnum

# import stack
#
# import queue
#
# import doubleLinkedList
#
# import classinstance

# import typingtestlogic


from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("<a href='https://www.flipkart.com/laptops/'>https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)