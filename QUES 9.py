string=str(input("ENTER A SENTENCE: "))
a=[]
count={}
a=string.split()
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)            