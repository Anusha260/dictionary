# d={"1":["a",'b'],"2":["c","d"]}
# for x in d["1"]:
#     for y in d["2"]:
#         print(x+y)

d={"1":["a",'b'],"2":["c","d"]}
d1=d.get("1")
d2=d.get("2")
i=0
while i<len(d1):
    j=0
    while j<len(d2):
        a=d1[i]+d2[j]
        print(a)
        j=j+1
    i=i+1

