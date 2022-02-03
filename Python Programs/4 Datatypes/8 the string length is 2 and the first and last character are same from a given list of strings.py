# Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

n=int(input("enter the number of string :"))
i =0
list1=[]
while i<n:
    num=input("enter the string:")
    list1.append(num)
    i=i+1
print(list1)
# list1=['abc', 'xyz', 'aba', '1221']
j=0
for x in list1:
    if len(x)>=3  and x[0]==x[-1]:
        print(x)
        j=j+1
print("no. of strings where string length is 2 or more and first and last char are same: ",j)

