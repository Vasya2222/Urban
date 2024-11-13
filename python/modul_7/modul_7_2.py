def custom_write(file_name, string):
    result = dict()
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, item in enumerate(string):
            byte = file.tell()
            file.write(item + '\n')

            result[(index + 1, byte)] = item

    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
print(result)
