dict={"name":"anusha","age":"21"}
a=input("enter the number")
for i in dict:

    if a in dict:
        print("key is present")
        break
    else:
        print("key is not present")
