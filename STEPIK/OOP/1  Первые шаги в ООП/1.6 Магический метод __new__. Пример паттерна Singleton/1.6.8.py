TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, name,  *args, **kwargs):
        __name = name
        if __name == 1:
            return DialogWindows()
        elif __name == 2:
            return DialogLinux()

    def __init__(self, name):
        self.name = name


dlg = Dialog(1)
print(dlg.name_class)
