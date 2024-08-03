my_dict = {
    'Vanya': 2000,
    'Vasya': 2003,
    'Varya': 1997
}

print('Dict:', my_dict)

print('Existing value:', my_dict.get('Vanya', 'Такого ключа нет'))
print('Not existing value:', my_dict.get('Natasha', 'Такого ключа нет'))

delete_item_in_my_dict = my_dict.pop('Vasya')
print('Deleted value:', delete_item_in_my_dict)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 6, 63, False, True, 'Hello', False, 1, 'Hello', True, 2, 4, 5}
print('Set:', my_set)

my_set.add(100)
my_set.add(1.5)
# my_set.add({'Masha': 111111111}) Я как-то раньше не интересовался можно ли добавлять словарь 
# в множество, но почему-то не получается, хотя должно, почему не получается? 
# А возможно ли добалять? Если да, то как? И со списком такая же история.
my_set.discard('Hello')

print('Modified set:', my_set)