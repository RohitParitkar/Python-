# 15.	WAP to input all sides of a triangle and check whether triangle is valid or not.

a= int(input("enter any value: "))
b= int(input("enter any value: "))
c= int(input("enter any value: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("it is a triangle")
else:
    print("it is not ")