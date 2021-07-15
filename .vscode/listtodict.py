v=[1,2,3,4,5,6]
k=["one","two","three","four","five"]
k.append("six")
d={}
i=0
while i<len(v):
    d[v[i]]=k[i]
    i=i+1
print(d)

