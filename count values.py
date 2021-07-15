dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34,35]}
b=[]
for i,j in dict.items():
    print(i,end=" ")
    b.append(j)
print()
i=0
while i<len(b):
    j=0
    while j<len(b):
        print(b[j][i],end=" ")
        j=j+1
    print()
    i=i+1
    a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
d={}
b=[]
for i in a.values():
    b.append(i)
j=0
while j<len(b):
    k=0
    c=0
    while k<len(b):
        if b[j]==b[k]:
            c=c+1
        k=k+1
    d.update({b[j]:c})    
    j=j+1
print(d)


    





