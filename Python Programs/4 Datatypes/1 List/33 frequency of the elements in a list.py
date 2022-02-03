entered_value=input("enter num: ")
s2=''
previous_index=-1
for x in entered_value:
    i=-1
    c=0
    while True:
        i = entered_value.find(x,i+1)   #i=(a,(-1+1))  i=(a,0) i=0 |i=(a,0) i=0 
        print("x:",x," ","i: ",i) 
        if i==-1:                       # 0 != -1                  |0!=-1
            break                       #                          |
        elif i-1==previous_index:                    # 0-1==-1                  |0-1==-1
            c=c+1                       # c=0+1 c=1                |c=0+1
            previous_index=i                         # p=0                      |p=0
    if c>0:                             # c>0 1>0                  |c>0 1>0
        s2=s2+str(c)+x                  # s2=0+1+a                 |s2=0+2+a
print(s2)
