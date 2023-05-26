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
    def __init__(self, ):
