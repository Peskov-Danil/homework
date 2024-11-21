my_dict= {'Данил': 1996, 'Антон': 1976 }
print(my_dict)
print(my_dict['Данил'])
print(my_dict.get('Артем'))
my_dict= {'Данил': 1996, 'Антон': 1976,'Ева':2001, 'Настя':2002 }
print(my_dict)
my_dict.pop('Настя')
print(my_dict)
my_set={1,2,3,4,4,7,7,'Fly','Fly',1,2,3,4,4,7,7,46.581,46.581}
print(my_set)
my_set={1, 2, 3, 4, 7, 46.581, 'Fly',False,(1,2,3)}
print(my_set)
my_set.discard(False)
print(my_set)