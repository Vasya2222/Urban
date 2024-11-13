def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        try:
            return str(a) + b
        except TypeError:
            return a + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))