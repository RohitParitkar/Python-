# 13 take any digit and print addition of first and last digit.py

n = int(input(" enter num: "))
a=n%10

i=1
add=0
while n>0:
    b=n%10
    n=n//10
print("the value of first value: ",b)
print("the value of last value: ",a)
add=a+b
print("addition: ",add)