first, second, third = int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))

if first == second == third:
    print(3)

elif first == second != third or first == third != second or second == third != first:
    print(2)

else:
    print(0)