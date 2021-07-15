list=[1,2,3,4]
d={}
dict=d
for i in list:
    d[i]={}
    d=d[i]
print(dict)