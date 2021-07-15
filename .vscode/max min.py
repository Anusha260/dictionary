my_dict = {'x':500, 'y':5874, 'z': 560}

max1=0
min=0

for i in my_dict:
    for j in my_dict:
        if my_dict[i]>max1:
            max1=my_dict[i]
        elif my_dict[i]<min:
            min=my_dict[i]
print(max1)
print(min)

        
    