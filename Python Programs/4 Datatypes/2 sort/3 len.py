mylist= ["aaaa","bbbbbb","c"]
print(mylist)
mylist.sort(reverse=True)
print("reverse",mylist)
mylist.sort(key=len)
print(mylist)
