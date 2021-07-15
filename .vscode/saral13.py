dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
max1=0
max2=0
max3=0
for i in dict:
    for j in dict:
        if dict[j]>max1:
            max1=dict[j]
            max1key=j
            
        elif max1>dict[j] and max2<dict[j]:
            max2=dict[j]
            max2key=j

        elif max2>dict[j] and max3<dict[j]:
            max3=dict[j]
            max3key=j
        else:
            pass
print(max1key)
print(max2key)
print(max3key)