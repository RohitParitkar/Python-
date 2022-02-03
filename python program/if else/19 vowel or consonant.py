# 8.	Write a C program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter any alphabet: ")
alpha = alpha.lower()
if alpha in("a,e,i,o,u"):
    print("vowel")
else:
    print("consonant")