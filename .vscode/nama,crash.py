list=[{"name":"anu","cash":40},{"name":"anusha","cash":50},{"name":"shailu","cash":60},{"name":"shailuja","cash":70}]
user=input("enter the name")
for i in list:
    s=""
    a=i["name"]
    
    if user in i["name"]:
        print(i)
sum=0
for j in list:
    sum=sum+j["cash"]
print(sum)