mounth = input("Enter the full name of the month you storing for : ")
salary = int(input("Enter your salary for this month : "))
saving = int(input("input the percentages for Savings : "))
savingamount = (saving * salary / 100)
rent = int(input("input the cost of rent for this mounth : "))
electricity = int(input("input the cost of electricity for this mounth : "))
print (f" The mounth is {mounth} ")
print (f" Your salary for this mounth is {salary} $ ")
print (f" Percentage of Saving is {saving} % , Which equals {savingamount} $")
print (f"The rent will cost you {rent} $ , Which is {(100*rent/salary)} % of your salary")
print (f"The electricity will cost you {electricity} $ , Which is {(100*electricity/salary)} % of your salary")