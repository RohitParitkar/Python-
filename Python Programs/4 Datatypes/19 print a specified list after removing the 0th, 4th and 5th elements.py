# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


mylist=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2=['Green', 'White', 'Black']
list3=[]
for i  in mylist:
    if i not in list2:
        list3.append(i)
print(list3)
        