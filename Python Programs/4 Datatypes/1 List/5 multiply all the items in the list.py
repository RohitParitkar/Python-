n = int(input("num of elements: "))
multiply=1
i=1

list=[]
while i<=n:
    x=int(input("enter the elements: "))
    list.append(x)
    i=i+1
print(list)
for c in list:
    multiply=multiply*c
print(multiply)


