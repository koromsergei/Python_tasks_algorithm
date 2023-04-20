class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):

        if not (type(string) is str) or not (self.min_length <= len(string) <= self.max_length):
            return False
        return True


class StringValue:
    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)
        else:
            pass


class RegisterForm:
    login = StringValue(validator=(ValidateString(1, 10)))
    password = StringValue(validator=(ValidateString(1, 10)))
    email = StringValue(validator=(ValidateString(1, 2)))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_field(self):
        print(self.login, self.password, self.email)

    def show(self):
        print('<form>',
              f'Login: {self.login}',
              f'Password: {self.password}',
              f'Email: {self.email}'
              '</form>', sep='\n')


form = RegisterForm('Sergei', 'df123l30L', 'w@gmail.com')
form.show()
form.get_field()
