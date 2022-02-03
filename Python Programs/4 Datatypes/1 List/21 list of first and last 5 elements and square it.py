#16. Write a Python program to generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30 (both included). 

listt=[]
for i in range(1,31):
	listt.append(i**2)
print(listt[:5])
print(listt[-5:])