# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
num=int(input("enter num of elements:"))
a=0
list1=[]
while a<num:
    x=input("enter values: ")
    list1.append(x)
    a=a+1
print('mylist',list1)

result=[]
n = int(input("enter the digit you want to check the words are longer than given number: "))
for i in list1:
    if len(i)>n:
        result.append(i)
print("result: ",result)
