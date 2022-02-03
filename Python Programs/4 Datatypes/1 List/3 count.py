# 1 WAP to print count of each item present in the list.(frequency count)
#   to find out how many types 1 aplhabet occured.

list=[]
while True:
    x = int(input("enter num: "))
    list.append(x)
    choice = input("Do you want to continue?(y/n)")
    if choice == 'n':
        break
print(list)
temp=[]
for i in list:
    if i not in temp:
        y= list.count(i)
        print(i,y)
        temp.append(i)

    