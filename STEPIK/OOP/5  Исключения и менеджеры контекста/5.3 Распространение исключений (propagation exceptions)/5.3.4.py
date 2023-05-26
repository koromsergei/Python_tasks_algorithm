class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_validate(self, string):
        if not (self.min_length <= len(string) <= self.max_length):
            raise ValueError
        elif self.chars == '':
            return string
        elif len(set(string) & set(self.chars)) == 0:
            raise ValueError
        return string


class LoginForm:
    def __init__(self, login_val: ValidatorString, pass_val: ValidatorString):
        self.login_val = login_val
        self.pass_val = pass_val
        self._login = None
        self._password = None

    def form(self, request: dict):
        try:
            lg = request['login']
            psw = request['password']
        except TypeError:
            print(e)
        self._login = self.login_val.is_validate(lg)
        self._password = self.pass_val.is_validate(psw)


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)

# login, password = input().split()
login, password = 'input().split()', '!!@#$!@#$!@#!@#%$#@'

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
