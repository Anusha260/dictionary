dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for k in dict:
    v=dict[k]
    a=[]
    for j in v:
    
        if j%2==0:
            a.append(j)
        dict[k]=a
print(dict)
        
        
    