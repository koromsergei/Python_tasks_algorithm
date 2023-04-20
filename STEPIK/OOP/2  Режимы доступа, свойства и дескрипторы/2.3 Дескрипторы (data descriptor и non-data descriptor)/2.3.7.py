class StringValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if not (type(string) is str) or self.min_length <= len(string) <= self.max_length:
            return False
        return True


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

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



from = RegisterForm('Login', 'Password', 'email')

