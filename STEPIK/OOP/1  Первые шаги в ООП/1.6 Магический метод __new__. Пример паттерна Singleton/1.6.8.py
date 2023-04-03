TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, name,  *args, **kwargs):
        __name = name
        if __name == 1:
            return DialogWindows.__new__(cls)
        elif __name == 2:
            return DialogLinux.__new__(cls)

    def __init__(self, name):
        self.name = name


dlg = Dialog(1)
print(dlg)
