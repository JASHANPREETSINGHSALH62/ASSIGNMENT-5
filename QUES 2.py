upper_num=int(input("ENTER THE UPPER RANGE: "))
lower_num=int(input("ENTER THE LOWER RANGE: "))
div=int(input("ENTER THE NUMBER THAT SHOULD BE DIVIDED: "))
for i in range(upper_num,lower_num+1):
    if(i%div==0):
        print(i)