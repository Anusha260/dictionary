dict1=[]
dict2=[]
dict={}
i=0
while i<10:
    n=int(input("enter the names"))
    m=input("enter the numbers")
    dict1.append(n)
    dict2.append(m)
i=i+1
j=0
while j<len(dict1):
    dict1[j]=dict2[j]
    j=j+1
print(dict)
    
    
    