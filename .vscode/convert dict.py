list=[1,2,3,4,5]
list1=["one","two","three","four","five"]
num=input("enter the number")
num_str=input("enter the number")

i=0
while i<len(list):
    list.append(num)
    list1.append(num_str)
    i=i+1
    a=dict(zip(list,list1))
    break
print(a)