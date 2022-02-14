# 2.	Write a C program to find maximum between three numbers.

num1= float(input("enter first value: "))
num2= float(input("enter second value: "))
num3= float(input("enter third value: "))

if (num1>num2) &( num1>num3):
    print("num1: ",num1)
elif (num2>num1) &( num2>num3):
    print("num2: ",num2)
else:
    print("num3: ",num3)