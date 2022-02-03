# 7. Write a Python program to remove duplicates from a list. 

n = int(input("number of elements: "))
a=0
mylist=[]
while a<n:
    x=input("enter values: ")
    mylist.append(x)
    a=a+1
print("The list is: ",mylist)

resultlist=[]
for i in mylist:
    if i not in resultlist:
        resultlist.append(i)
print("the answer: ",resultlist)