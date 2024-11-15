first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(word[0]) - len(word[1]) for word in zip(first, second) if len(word[0]) != len(word[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))