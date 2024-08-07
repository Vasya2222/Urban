from time import sleep


class UrTube():
    
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print('Hello', nickname)
                break
        else:
            print('Такого пользователя/пароля нет')
    
    def register(self, nickname, password, age):
        flag = False
        for user in self.users:
            if  nickname == user.nickname:
                flag = True
                break
        if flag:
            print(f'Пользователь {nickname} уже существует')
        else:
            create_user = User(nickname, hash(password), age)
            self.users.append(create_user)
            self.current_user = create_user

    def log_out(self):
        self.current_user = None
    
    def add(self, *args):
        for video in args:
            should_add = True
            for check_video in self.videos:
                if video.title == check_video.title:
                    should_add = False
                    break
    
            if should_add:
                self.videos.append(video)


    def get_videos(self, search_title_video):
        list_videos = list()
        for video in self.videos:
            if search_title_video.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos if len(list_videos) > 0 else 'Видео с таким названием нет'
    
    def watch_video(self, title_video):
        for video in self.videos:
            if title_video.lower() == video.title.lower():
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                else:
                    if self.current_user.age >= 18 and video.adult_mode == True:
                        for second in range(video.duration + 1):
                            
                            print(second, end=' ', flush=True)
                            sleep(1)
                            
                        print('Конец видео')
                    elif self.current_user.age < 18 and video.adult_mode == False:
                        for second in range(video.duration):
                            print(second, end=' ')
                            sleep(1)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        
        def __str__(self):
            return self.current_user.nickname
    


    





    


class Video():


    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User():

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')