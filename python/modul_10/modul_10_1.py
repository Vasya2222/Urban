import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(f'example/{file_name}', 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # сделать паузу 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")


start_time = time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time()
print(f"Время выполнения для первых четырех вызовов: {end_time - start_time:.2f} секунд")

# Функция для запуска в потоке
def threaded_write_words(word_count, file_name):
    write_words(word_count, file_name)

# Создание потоков
threads = []
start_time_threads = time()
threads.append(threading.Thread(target=threaded_write_words, args=(10, "example5.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(30, "example6.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(200, "example7.txt")))
threads.append(threading.Thread(target=threaded_write_words, args=(100, "example8.txt")))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()
end_time_threads = time()
print(f"Время выполнения для потоков: {end_time_threads - start_time_threads:.2f} секунд")