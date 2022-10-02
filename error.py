
try:
    # number = 10/0
    num = int(input('Enter a number'))
    num = num /10
    print(num)

# except:
#     print('err occured in the code')
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
    print('cant divide a number  by 0')

