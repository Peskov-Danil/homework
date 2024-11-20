immutable_var= 1,2,True,"Фрога"
print(type (immutable_var))
immutable_var_2=[1,2,True,"Фрога"]
immutable_var=immutable_var_2
# равенство дает понять , что это один тип данных кортеж, immutable_var_2
# введен в виде списка,а immutable_var введен в виде кортежа, из этого следует , что
# кортеж изменить нельзя, хотя внутри его можно редактировать.
mutable_list=[1,2,3,4]
mutable_list.append(5)
mutable_list.extend('Фрога')
print(mutable_list )