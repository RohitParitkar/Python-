# 23. Write a Python program to flatten a shallow list. 

n=[['a','b','c'],['d','e','f'],['g','h','i']]
result=[]
for sublist in n:
    for items in sublist:
        result.append(items)
print(result)