

file_ = open('employee.txt','r+')
if file_.readable():
    # print(file_.read())
    print(file_.readline())
    # print(file_.readlines())
    for emp in file_.readlines():
        print(emp)

file_.close()