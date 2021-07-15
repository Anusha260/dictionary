num=[12,23,10,22]

i=0
b=[]
while i<len(num):
    sum=0
    
    while num[i]>0:
        a=num[i]%10
        sum=sum+a
        num[i]=num[i]//10
        
    b.append(sum)
    i=i+1
print(b)