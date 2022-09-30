

def tds_calculator(salary,monthly):
    if monthly is True:
        salary = salary * 12
    print(salary)
    if salary > 1500000:
        return salary*30/100
    elif salary > 1250000 and salary <= 1500000:
        return salary*25/100
    elif salary > 1000000 and salary <= 1250000:
        return salary*20/100
    elif salary >750000 and salary <= 1000000:
        return salary*15/100
    elif salary > 500000 and salary <= 750000 :
        return salary*10/100
    elif salary > 250000 and salary <= 500000:
        return salary*5/100
    else:
        return "No TDS"
    # return salary*25/100 if  else return salary