
file_ = open('employee.txt','r+')
if file_.readable():
    # print(file_.read())
    print(file_.readline())
    # print(file_.readlines())
    for emp in file_.readlines():
        print(emp)

file_.close()


do_write = True if int(input('Enter 0 or 1')) == 1 else False

if do_write:
    file_w = open('employee.txt','a')
    content = input('Enter the value name and designation')
    file_w.write(content)
    file_w.close()

