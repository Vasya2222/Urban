def print_params(a=1, b='String', c=True):
    print(a, b, c)

print_params()
print_params(a=1.5)
print_params(b=False)
print_params(a={'Vasya': 21}, b=(1, 3,5, True, False, [1, 3, 5]), c=[1, True, [1, 34]])

value_list = [1, 'Text', True]
value_dict = {
    'a': 21,
    'b': True,
    'c': False
}

print_params(*value_list)

print_params(**value_dict)

value_list_2 = [True, False]

print_params(*value_list_2, 42)
