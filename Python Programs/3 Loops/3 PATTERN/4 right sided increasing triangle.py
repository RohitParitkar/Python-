n = int(input("num: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end="") #give sapce between double quotes(" ") 
    for j in range(i+1):
        print("*",end="")
    print("")