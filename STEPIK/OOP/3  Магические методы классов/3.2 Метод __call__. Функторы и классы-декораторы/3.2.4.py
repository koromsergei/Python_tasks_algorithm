from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator

class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        name = args[0]
        if self.min_length <= len(name) <= self.max_length:
            return True
        return False


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        name = args[0]
        if set(name).issubset(set(self.chars)):
            return True
        return False


lg = LoginForm('Entry', validators=[LengthValidator(4, 30), CharsValidator(ascii_lowercase + digits)] )
lg.post({'login': 'root', 'password': 'gatos'})
print(lg.is_validate())
