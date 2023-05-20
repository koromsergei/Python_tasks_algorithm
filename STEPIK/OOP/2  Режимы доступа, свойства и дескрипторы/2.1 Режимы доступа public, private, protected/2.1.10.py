from string import digits, ascii_letters
import random


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        all_sights = digits + ascii_letters + '.' + '_'
        email = ''
        for i in range(random.randint(1, 100)):
            email += random.choice(all_sights)
        return email + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return type(email) is str

    @classmethod
    def check_email(cls, email):
        allowed_text = digits + ascii_letters + '.' + '_' + '@'
        if not(cls.__is_email_str(email)):
            return False
        if email.count('@') > 1:
            return False
        if not(set(email).issubset(set(allowed_text))):
            return False
        bf_at, af_at = email.split('@')
        if len(bf_at) > 101 or len(af_at) > 50:
            return False
        if af_at.count('.') == 0:
            return False
        for i in range(len(email) - 1):
            if email[i] == '.':
                if email[i + 1] == '.':
                    return False
        return True


print(EmailValidator.get_random_email())
print(EmailValidator.check_email('asdas324d@gmail.com'))

print(EmailValidator.check_email(EmailValidator.get_random_email()))
