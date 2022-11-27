class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    app_store = dict()

    @classmethod
    def add_application(cls, app):
        cls.app_store.update({app.name: app.blocked})


    @classmethod
    def remove_application(cls, app):
        cls.app_store.pop(app.name)

    @classmethod
    def block_application(cls, app):
        app.blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.app_store)


store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)

assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"
