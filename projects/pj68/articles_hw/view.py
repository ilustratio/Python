def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действия с фильмами")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_user_article(self):
        dict_article = {
            "Название фильма": None,
            "Жанр": None,
            "Режиссер": None,
            "Год выпуска": None,
            "Длительность": None,
            "Студия": None,
            "Актеры": None
        }
        for key in dict_article:
            dict_article[key] = input(f"{key}: ")
        return dict_article

    @add_title("Каталог фильмов")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')

    @add_title("Ввод названия фильма")
    def get_user_article(self):
        user_article = input("Введите название фильма: ")
        return user_article

    @add_title("Просмотр информации о фильме")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} - {article[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f'Фильма с названием {user_title} не существует')

    @add_title("Удаление фильма")
    def remove_single_article(self, article):
        print(f'Фильм {article} - был удален')

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f'Вариант {answer} не существует')
