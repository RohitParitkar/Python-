# 1.	    

n = int (input("enter num: "))
i =0 
mylist=[]
while i<n:
    x=input("enter values: ")
    mylist.append(x)
    i=i+1
print(mylist)

t=mylist[0]
mylist[0]= mylist[n-1]
mylist[n-1]=t
print(mylist)