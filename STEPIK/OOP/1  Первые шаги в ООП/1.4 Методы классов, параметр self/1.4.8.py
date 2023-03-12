class String_type:
    to_empty = 12

    def __init__(self):
        self.is_empty = False


s1 = String_type()
print(s1.is_empty)
s1.to_empty = 132
print(String_type.to_empty)
