# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
n = [1,2,3,4,5,6,7,8,9,10]
print("list: ",n)
for i in n:
    if i%2==0:
        n.remove(i)
print("ans=",n)
