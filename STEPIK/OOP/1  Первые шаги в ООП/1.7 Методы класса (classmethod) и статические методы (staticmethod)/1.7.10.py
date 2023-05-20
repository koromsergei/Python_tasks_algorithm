class Application:
    def __init__(self, name: str):
        self.blocked = False
        self.name = name


class AppStore:
    def __init__(self):
        self.app_list = []

    def add_application(self, app: Application):
        self.app_list.append(app)

    def remove_application(self, app: Application):
        self.app_list.remove(app)

    @staticmethod
    def block_application(self, app: Application):
        app.blocked = False

    def total_apps(self):
        print(len(self.app_list))
        return len(self.app_list)

store = AppStore()
app_youtube = Application('YouTube')
store.add_application(app_youtube)
store.block_application()
store.total_apps()

