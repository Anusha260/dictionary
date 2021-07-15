word _dict={'bijender':45,'deepak':60,'param':20,';'anu':30,'roshini':50}
sorted_dict = dict( sorted(word_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))
print('Sorted Dictionary: ')
print(sorted_dict)
