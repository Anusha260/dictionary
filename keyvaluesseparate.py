
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
a=[]

for i,j in my_dict.items():
    print(i,end=" ")
    a.append(j)
print()
i=0
while i<len(a):
    j=0
    while j<len(a):
        print(a[j][i],end=" ")
        j=j+1
    print()
    i=i+1
    


