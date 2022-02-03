# # *****
# #    *
# #   *
# #  *
# # *****

for i in range(0,5):
    for j in range(0,5+1):
        if i==0 or i==4 or i+j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
