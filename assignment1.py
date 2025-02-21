mounth = input("Enter the full name of the month you storing for : ")
salary = int(input("Enter your salary for this month : "))
saving = int(input("Input the percentages for Savings : "))
savingamount = (saving * salary / 100)
rent = int(input("Input the cost of rent for this mounth : "))
electricity = int(input("Input the cost of electricity for this mounth : "))

def initCalculator():
    TheMonth = input("Enter the name of the month : ")
    TheSalary = int(input("Enter your salary for this month : "))
    new = { 
        "user" : 'Nabiha',
        "date" : TheMonth,
        "Salary" : TheSalary,
    }

    return new

def TheMath():
    saving = float(input("Enter the percentage of saving: "))
    rent = int(input("Input the cost of rent for this mounth : "))
    electricity = int(input("Input the cost of electricity for this mounth : "))
    x = saving * salary
    x1 = x + rent + electricity
    if x1 > salary :
        print ("you spend more than your salary")
    else :
        print (f" The mounth is {mounth} ")
        print (f" Your salary for this mounth is {salary} $ ")
        print (f" Percentage of Saving is {saving} % , Which equals {savingamount} $")
        print (f"The rent will cost you {rent} $ , Which is {round((100*rent/salary),2)} % of your salary")
        print (f"The electricity will cost you {electricity} $ , Which is {round((100*electricity/salary),2)} % of your salary")