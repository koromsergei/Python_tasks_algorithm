import sys


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self):
        self.inbox_lst = None

    def receive(self):
        lst = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_lst = [MailItem(*i.split()) for i in lst]


mail = MailBox()
mail.receive()
mail.inbox_lst[0].is_read = False
fl = filter(bool, mail.inbox_lst)
print(fl)
