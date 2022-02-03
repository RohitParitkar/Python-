# 11. Write a Python function that takes two lists and returns True if they have at least one common member. 



mylist1=[1,2,3,4,5,6]
mylist2=[10,20,30,3,2]
list3=[]
for i in mylist1:
    if i in mylist2:
        if i not in list3:
            list3.append(i)

print("list3",list3)