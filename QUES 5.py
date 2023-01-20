n=int(input("ENTER NUMBER OF ROWS :"))
a=ord("A")
for i in range (n+1):
    for j in range (i):
        print(chr(a),end="")
        a=a+1
    print()    