dict={"h":"red","m":"red","s":"green","k":"black","g":"green"}
s=""
for i in dict:
    for j in dict:
        if i==j and i!="k":
            s=i
            print(s)