

def initCalculator():
    print('-----------------------------------------------')
    new = { 
        "user" : 'Nabiha',
        "date" : month ,
        "Salary" : salary ,
    }
    print (new)

    return new

def TheMath():
    x = saving * salary / 100
    x1 = x + rent + electricity
    if x1 > salary :
        print ("you spend more than your salary")
    else :
        print ("**************************************************")
        print (f"The mounth is {month} Your salary for this mounth is {salary} $\n ")
        print (f"Percentage of Saving is {saving} % , Which equals {savingamount} $\n")
        print (f"The rent will cost you {rent} $ , Which is {round((100*rent/salary),2)} % of your salary \n")
        print (f"The electricity will cost you {electricity} $ , Which is {round((100*electricity/salary),2)} % of your salary\n")
        print (f'The total amount you spends equals to {x1} $ , thus you have now {salary-x1} $')
        print ("**************************************************")
        print (f"your emestimate yearly rent and electricity costs equals to {(x1-x)*12} $.\n")
        print (f"Salary will not see Nabiha {(salary**2)} $\n")



month = input("Enter the full name of the month you storing for : ")
salary = int(input("Enter your salary for this month : "))
saving = int(input("Input the percentages for Savings : "))
savingamount = (saving * salary / 100)
rent = int(input("Input the cost of rent for this mounth : "))
electricity = int(input("Input the cost of electricity for this mounth : "))

initCalculator()
TheMath()
print(f"With the additional 50 $")
salary = salary + 50
initCalculator()
TheMath()
