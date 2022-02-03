n = int(input(" num: "))
sum=0
a= n%10
while n>0:
    b=n%10
    n=n//10
sum=b+a
print(sum)