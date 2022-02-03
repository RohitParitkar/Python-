# 29. Write a Python program to get unique values from a list. 
mylist=[1,2,3,7,8,9,8,7,1,4]
new=[]
for i in mylist:
    if i not in new:
        new.append(i)
print(new)