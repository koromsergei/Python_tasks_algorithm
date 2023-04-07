from accessify import private, protected


class Clock:
    def __init__(self, __time):
        self.__time = __time if self.__check_time(__time) else 0

    @staticmethod
    def __check_time(tm):
        if type(tm) is int and 0 <= tm < 100000:
            return True
        return False

    def set_time(self, tm):
        self.__time = tm if self.__check_time(tm) else self.__time

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(2)
print(clock.get_time())
