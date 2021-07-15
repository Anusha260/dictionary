num=int(input("enter the number"))
a=0
j=num
while True:
    if j%2==0:
        print(j)
        a+=1
    if a==3:
        break
    j-=1        
c=0
while True:
    if num%2!=0:
        print(num)        
        c=c+1
    if c==3:    
        break
    num+=1
    