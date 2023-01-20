a=[]
positive_numbers=[]
negative_numbers=[]
odd_numbers=[]
even_numbers=[]
count={}
for i in range(10):
    print("ENTER NUMBER",i+1,(": "),end="")
    nbr=int(input())
    a.append(nbr)
for p in a:
    if(p>0):
        if p not in positive_numbers:
            positive_numbers.append(p)
    elif(p<0):
        if p not in negative_numbers:
            negative_numbers.append(p)                
for e in a:
    if(e%2==0 or e==0):
        if e not in even_numbers:
            even_numbers.append(e)
    else:
        if e not in odd_numbers:
            odd_numbers.append(e)
print()            
print("1)POSITIVE NUMBERS ARE:",positive_numbers,"\n")
print("2)NEGATIVE NUMBERS ARE:",negative_numbers,"\n")
print("3)ODD NUMBERS ARE:",odd_numbers,"\n")
print("4)EVEN NUMBERS ARE:",even_numbers,"\n")
print("5)NUMBER OF TIMES EACH NUMBER OCCURS IN LIST ARE GIVEN BELOW:")                                   
for element in a:
    if element in count:
        count[element]+=1
    else:
        count[element]=1
for key,value in count.items():
    print(key,"     OCCURS    ",value,"   TIMES")       
