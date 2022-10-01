import time

def cal_bigO():
    timestamp1 = time.time()

    number = 100000
    total = 0
    for value in range(number):
        total+= value

    print('the sum is ',total)

    timestamp2 = time.time()

    print(timestamp2-timestamp1)

def cal_while_bigO():
    timestamp1 = time.time()

    number = 100000
    total = 0
    i=0
    while i< number:
        total+= i
        i+=1

    print('the sum is ',total)

    timestamp2 = time.time()

    print(timestamp2-timestamp1)
