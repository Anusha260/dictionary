list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
i=0
d={}
while i<len(list1):
    d[list1[i]]=list2[i]
    i=i+1
print(d)