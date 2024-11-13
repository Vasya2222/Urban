import os
import time

# Укажите путь к директории, которую хотите обойти
directory = r'E:\Py\Urban\python'

# Проверяем, существует ли директория
if not os.path.exists(directory):
    print(f"Директория {directory} не найдена.")
else:
    # Проходим по всем подкаталогам и файлам в указанной директории
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Формируем полный путь к файлу
            filepath = os.path.join(dirpath, filename)

            # Получаем время последнего изменения
            mtime = os.path.getmtime(filepath)
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))

            # Получаем размер файла
            file_size = os.path.getsize(filepath)

            # Получаем родительскую директорию
            parent_directory = os.path.dirname(filepath)

            # Вывод информации о файле
            print(f"Файл: {filename}")
            print(f"Полный путь: {filepath}")
            print(f"Родительская директория: {parent_directory}")
            print(f"Размер: {file_size} байт")
            print(f"Последнее изменение: {formatted_time}")
            print("-" * 40)
