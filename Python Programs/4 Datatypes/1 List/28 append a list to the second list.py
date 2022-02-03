# 24. Write a Python program to append a list to the second list. 

list1=[1,2,3,4,5,6,7,8,9]
list2=["abc","def","ghi"]
print("list 1: ",list1)
print("list 2: ",list2)

list3=[]
for i in (list1 + list2):
    list3.append(i)
print("list 3: ",list3)