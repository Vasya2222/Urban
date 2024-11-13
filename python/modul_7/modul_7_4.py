# %
team1_num = 10
team2_num = 12
print("В команде Мастера кода участников: %s! " % team1_num)

print("В команде Мастера кода участников: %s и %s! " % (team1_num, team2_num))

# format

score_2 = 100
print("Команда Волшебники данных решила задач: {0}! ".format(score_2))

team1_time = 20000.3

print("Волшебники данных решили задачи за {0}c !".format(team1_time))

# f-str

score_1 = 50

print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = "Победа команды Волшебники данных!"
print(f'Результат битвы: {challenge_result}')

tasks_total = 500
time_avg = 40

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
