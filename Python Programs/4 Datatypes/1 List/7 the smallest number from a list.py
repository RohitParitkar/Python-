n= int(input("enter the number of digits : "))
list=[]
i=0
while i<n:
    num=int(input("enter the num : "))
    list.append(num)
    i=i+1
print(list)
list.sort()
print("the minmum number of the list is: ",list[0])
mini=min(list)
print("minimum",mini)

