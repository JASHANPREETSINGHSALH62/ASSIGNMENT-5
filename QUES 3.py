a=float(input("ENTER FIRST SIDE OF TRIANGLE: "))
b=float(input("ENTER SECOND SIDE OF TRIANGLE: "))
c=float(input("ENTER THIRD SIDE OF TRIANGLE: "))
s=a+b+c/2
if((a+b>c and a+c>b and b+c>a) and (a!=0 and b!=0 and c!=0)):
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("AREA OF THE TRIANGLE IS: ",round(area,2))
else:
    print("TRIANGLE NOT POSSIBLE")