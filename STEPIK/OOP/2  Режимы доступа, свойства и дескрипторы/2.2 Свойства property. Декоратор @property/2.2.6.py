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
    def next(self, next_elem):
        if type(next_elem) in (None, StackObj):
            self.__next = next_elem


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
            self.last = obj
            return
        self.last.next = obj
        self.last = obj
        return

    def pop(self):
        self.last = None

    def get_data(self):
        link = self.top
        print(link.data, end=' ')
        while link is not None:
            print(link.next.data, end=' ')
            link = link.next


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))
st.push(StackObj('obj4'))
print(st.last.next, st.top.next.next.data)
print(st.get_data())
# st.pop()
# print(st.get_data())
