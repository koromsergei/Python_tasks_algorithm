class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    __instance = None
    lst_msg = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def add_message(cls, msg: Message):
        cls.lst_msg.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.lst_msg.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = True

    @classmethod
    def show_last_message(cls):
        return cls.lst_msg[-1]

    @classmethod
    def total_message(cls):
        return len(cls.lst_msg)


msg = Message('Hello World!')
Viber.add_message(msg)
print(Viber.total_message())
