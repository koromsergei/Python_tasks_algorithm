import sys

# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
lst_in = ['1st link', '2nd link', '3rd link', '4th link']
# здесь создаются объекты классов и вызываются нужные методы


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


head_obj = ListObject(lst_in[0])

two_obj = ListObject(lst_in[1])
two_obj.link(head_obj)

three_obj = ListObject(lst_in[2])
three_obj.link(two_obj)

three_obj.next_obj