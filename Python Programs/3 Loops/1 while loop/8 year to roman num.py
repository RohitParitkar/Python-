# I=1 V=5 X=10 L=50 C=100 D=500 M= 1000

n = int(input("enter num:"))
while n>0:
    if n>=1000:
        print("M",end='')
        n=n-1000
    elif n>=500:
        print("D",end='')
        n=n-500
    elif n>=400:
        print("CD",end='')
        n=n-400    
    elif n>=100:
        print("C",end='')
        n=n-100
    elif n>=50:
        print("L",end='')
        n=n-50
    elif n>=10:
        print("X",end='')
        n=n-10
    elif n>=9:
        print("IX",end='')
        n=n-9
    elif n>=8:
        print("VIII",end='')
        n=n-8
    elif n>=7:
        print("VII",end='')
        n=n-7
    elif n>=6:
        print("VI",end='')
        n=n-6
    elif n>=5:
        print("V",end='')
        n=n-5
    elif n>=4:
        print("IV",end='')
        n=n-4
    elif n>=3:
        print("III",end='')
        n=n-3
    elif n>=2:
        print("II",end='')
        n=n-2
    else:
        print("I",end='')
        n=n-1