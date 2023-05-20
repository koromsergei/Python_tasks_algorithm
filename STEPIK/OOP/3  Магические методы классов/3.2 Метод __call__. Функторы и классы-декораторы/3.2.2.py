from random import randint
from string import ascii_lowercase, digits


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        psw = []
        ps_len = randint(self.min_length, self.max_length)
        for i in range(ps_len):
            psw.append(self.psw_chars[randint(0, len(self.psw_chars) - 1)])
        return ''.join(psw)


rnd = RandomPassword(ascii_lowercase + digits + '!@#$%&*', 6, 30)
psw = rnd()
psw1 = rnd()
psw2 = rnd()
print(psw, psw1, psw2, sep='\n')
print()


def password():

    def rnd_psw(psw_chars, min_length, max_length):
        psw = None
        if psw is None:
            psw = []
            ps_len = randint(min_length, max_length)
            for i in range(ps_len):
                psw.append(psw_chars[randint(0, len(psw_chars) - 1)])
            return ''.join(psw)
    return rnd_psw


ps = password()
