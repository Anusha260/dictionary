dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for value in dict:
    valuelist=dict[value]
    c1=len(valuelist)
    c=c+c1
print(c)




