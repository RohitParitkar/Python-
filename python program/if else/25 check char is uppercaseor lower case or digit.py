from ctypes.wintypes import PLARGE_INTEGER


ch = input("Enter Character: ")
char = ord(ch)
print(char)
if (97<=char<=122):
    print("It is Lowercase Letter and ASCII value of",ch,"is",char)
elif(65<=char<=90):
    print("It is Uppercase Letter and ASCII value of",ch,"is",char)
elif(48<=char<=57):
    print("It is a Number and ASCII value of",ch,"is",char)
else:
    print("enter valid number.")