#1.Write a Program to calculate Gross Salary.
#  In this program we will take basic salary as an input and on the basis of following calculations 
# we calculate gross salary.
# • da is 20% of basic salary
# • hra is 40% of basic salary
# • Gross Salary = basic salary + da + hra

basic_salary = float(input("Enter the gross salary:"))
da = (20/100)*basic_salary
print("the da is: ",da)
hra = (40/100)*basic_salary
print("hra is: ",hra)
Gross_Salary = basic_salary+da+hra
print("Gross Salary is: ",Gross_Salary)