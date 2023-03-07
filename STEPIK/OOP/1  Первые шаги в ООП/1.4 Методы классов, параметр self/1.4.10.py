class Translator:
    def __init__(self):
        self.dictionary = {}

    def add_words(self, eng: str, rus: str):
        if eng not in self.dictionary:
            self.dictionary[eng] = [rus]
        else:
            temp = self.dictionary.pop(eng)
            self.dictionary[eng] = [rus, *temp]

    def remove_words(self, eng):
        self.dictionary.pop(eng)

    def translate_words(self, eng):
        return self.dictionary.get(eng)


tr = Translator()
tr.add_words('go', 'поехать')
tr.add_words('go', 'отправиться')
tr.add_words('go', 'ехать')
tr.add_words('take', 'взять')
tr.add_words('cut', 'отрезать')

print(*tr.translate_words('cut'))
print(*tr.translate_words('go'))