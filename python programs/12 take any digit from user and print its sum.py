# #Wap o take any number from user and print its summation 
# from stat import IO_REPARSE_TAG_APPEXECLINK


n = int(input("enter any digit number: "))
add=0
while n>0:
    c=n%10
    n=n//10
    add=c+add
print(add)


