a= int(input("Enter three digit value: "))
b=a//100
print("the first value is: ",b)
c=a%100
d=c//10
print("the second value is: ",d)
e=c%10
print("the third value is: ",e)
reverse= b+d*10+e*100
print("the reverse value of the three digit is: ",reverse)