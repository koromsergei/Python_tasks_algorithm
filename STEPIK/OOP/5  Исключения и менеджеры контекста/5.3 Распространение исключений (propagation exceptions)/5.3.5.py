from abc import abstractmethod


class CustomTest:
    def __init__(self, descr):
        if 10 <= descr <= 100000:
            self.descr = descr
        else:
            raise ValueError('descr is more or less then the range')

    @abstractmethod
    def run(self):
        pass


class TestAnsDigit(CustomTest):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
