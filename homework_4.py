immutable_var = (1, True, [1, 2], 'string')
print(immutable_var)
# Задание 3: Попытайтесь изменить элементы кортежа immutable_var.
# Объясните, почему нельзя изменить значения элементов кортежа.
immutable_var[2][1] = 777
print(immutable_var) #Переменные в кортеже неизменные. Могу изменить только список внутри кортежа


mutable_list = [123, 'string', False, 0.25]
mutable_list.append('asd')
mutable_list[1] = 'строка'
print(mutable_list)
