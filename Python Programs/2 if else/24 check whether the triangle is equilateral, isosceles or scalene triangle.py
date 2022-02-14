a= int(input("enter any value: "))
b= int(input("enter any value: "))
c= int(input("enter any value: "))

#equilateral
if (a==b) and (a==c):
    print("it is equilateral")
elif (a==b) or (a!=b):
    print("it is isosceles ")
elif (a==c) or (a!=c):
    print("it is isosceles ")
else:
    print("it is scalene ")