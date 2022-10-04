

def arr_to_num(arr):
    return int("".join([ str(x) for x in arr]))
num = int(input('Enter a four digit number : '))

pre_num = 0
count = 0

while pre_num != num:
    pre_num = num
    num_arr = [int(x) for x in str(num)]
    # num1= int(sorted(num_arr).join('-'))
    num1= sorted(num_arr,reverse=True)
    num2= sorted(num_arr)
    num1 = arr_to_num(num1)
    num2 = arr_to_num(num2)
    num = num1-num2
    count+=1
    print(num,count)

print('mysterious number occured on ',count-1, ' iteration')

