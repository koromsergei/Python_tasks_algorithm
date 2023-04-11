class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) is (None, StackObj):
            self.__next = next


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
            return

        if self.last is None:
            self.last = obj



        obj.next


    def pop(self):
        pass

    def get_data(self, link=None):
        if link is None:
            link = self.top
        if link.next is None:
            return link.data
        else:
            # self.lst.append(link.next)
            link = link.next
            return self.get_data(link)


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))
st.push(StackObj('obj4'))
print(st.get_data())
