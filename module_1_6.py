my_dict={'Atlas':2254532,'Lada':1254112,'GAC':3251445}
print(my_dict)#Выведите на экран словарь
print(my_dict['GAC'])#Выведите на экран одно значение по существующему ключу
print(my_dict.get('Li'))#одно по отсутствующему из словаря my_dict без ошибки
my_dict.update({'Jac':1785142,'HQ':4257412})#Добавьте ещё две произвольные пары
print(my_dict)
my_dict.pop('Jac') #Удалите одну из пар в словаре по существующему ключу
print(my_dict.values()) #вывести значение из удаленной пары на экран не понятно как ЗНАК ВОПРОСА
print(my_dict)#Выведите на экран словарь


#Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями
my_set={1,2,3,'world',True,1,2}
#Выведите на экран множество my_set должны отобразиться только уникальные значения
print(my_set)
#Добавьте 2 произвольных элемента во множество my_set, которых ещё нет.
print(my_set.add(4))
print(my_set.add(5))
print(my_set)
#Удалите один любой элемент из множества my_set.
print(my_set.discard(2))
#Выведите на экран измененное множество my_set.
print(my_set)