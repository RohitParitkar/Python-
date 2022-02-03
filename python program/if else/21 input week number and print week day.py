# 11.	Write a C program to input week number and print week day.
week_num = int(input("enter week number: "))
if week_num == 1:
    print("monday")
elif week_num==2:
    print("tuesday")
elif week_num==3:
    print("wednesday")
elif week_num==4:
    print("thursday")
elif week_num==5:
    print("friday")
elif week_num==6:
    print("saturday")
elif week_num==7:
    print("sunday")
else:
    print("enter valid num")
