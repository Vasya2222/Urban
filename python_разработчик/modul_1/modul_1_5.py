immutable_var = (1, 1.5, 'String', True, [1, 0, 1], (1, 2, 3))
print(immutable_var)

# будет ошибка т.к кортеж является неизменяемым
immutable_var[0] = 2

mutable_list = [1, 1.5, 'String', True, [1, 0, 1], (1, 2, 3)]

mutable_list[1] = 'String'
mutable_list[4] = (1, 1.5, 'String', True, [1, 0, 1], (1, 2, 3))
mutable_list[0] = False

print(mutable_list)