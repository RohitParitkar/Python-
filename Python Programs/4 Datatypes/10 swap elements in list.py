# #swap two elements in list

# pos1= int(input("enter first num: "))
# pos2= int(input("enter second num: "))

# # Swap function
# def swapList(sl,pos1,pos2):
#     n = len(sl)     
#     # Swapping 
#     temp = sl[pos1]
#     sl[pos1] = sl[pos2]
#     sl[pos2] = temp
#     return sl      

# sl= [10, 14, 5, 9, 56, 12]
# # pos1= 2
# # pos2= 5

# print(sl)
# print("Swapped list: ",swapList(sl,pos1,pos2))

list1=[10, 14, 5, 9, 56, 12]
print(list1)
pos1=int(input("num1: "))
pos2=int(input("num2: "))

n=len(list1)
temp = list1[pos1]
list1[pos1] = list1[pos2]
list1[pos2] = temp

print(list1)