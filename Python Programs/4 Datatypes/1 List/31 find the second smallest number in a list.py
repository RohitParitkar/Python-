# 27. Write a Python program to find the second smallest number in a list. 

mylist=[3,5,7,1,6,8,8,3,5,7,9,3,5,71]
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[j]>mylist[j+1]:
            t=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=t
print(mylist)

second_smallest=mylist[1]
print("second_smallest:",second_smallest)

second_largest=mylist[-2]
print("second_largest: ",second_largest)
