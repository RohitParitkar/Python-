#get the largest number from a list. 
n = int(input("enter the number of elements in list: "))
list=[]
i =1
while i<=n:
    x=int(input("enter the num: ")) 
    list.append(x)
    i=i+1
print(list)
list.sort()
print(list[-1])
