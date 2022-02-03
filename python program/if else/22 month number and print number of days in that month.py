# 12.	Write a C program to input month number and print number of days in that month.

a = int(input("enter the month number: "))

if (a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
    print("This month have 31 days.")
elif (a==4 or a==6 or a==9 or a==11):
    print("This month have 30 days.")
elif (a==2):
    print("this month have 28 or 29 days.")
else:
    print("enter vaild number.")