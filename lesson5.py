immutable_var = 1, 3, 5, False, 'Одно кольцо чтоб править всеми'
print(immutable_var)
#immutable_var [3] = 8
#print(immutable_var) - элементы кортежа нельзя менять, т.к. кортежи не поддерживают обращение по элементам, они используются в основном как хранилище для списков, которые мы не хотим никак изменять и вообще трогать
mutable_list = ([2, 4, 6], True, 'Winter is coming')
print(mutable_list)
mutable_list [0][1] = 'Платформа 9 и 3/4'
print(mutable_list)