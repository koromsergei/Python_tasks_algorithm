from string import ascii_lowercase, digits

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class=\'login\'><{self.name}>: <input type=\'text\' size=<{self.size}> />'

    @classmethod
    def check_name(cls, name):
        print(set(name).issubset(set(cls.CHARS_CORRECT)))
        if 3 <= len(name) <= 50 and (set(name).issubset(set(cls.CHARS_CORRECT))):
            pass
        else:
            raise ValueError("некорректное поле name")
        return


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class=\'password\'><{self.name}>: <input type=\'text\' size=<{self.size}> />'

    @classmethod
    def check_name(cls, name):
        print(set(name) < set(cls.CHARS_CORRECT))
        if 3 <= len(name) <= 50 and (set(name).issubset(set(cls.CHARS_CORRECT))):
            pass
        else:
            raise ValueError("некорректное поле name")
        return

login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

name = "олдваылжав"
size = len(name)

login_check = TextInput(name, size)
login_check.check_name(name)
psw = PasswordInput(name, size)
