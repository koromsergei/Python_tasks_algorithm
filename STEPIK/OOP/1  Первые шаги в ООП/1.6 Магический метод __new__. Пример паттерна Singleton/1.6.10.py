# Здесь объявляется класс Factory
class Factory:
    @staticmethod
    def build_sequence():
        return []

    def build_number(self, sub):
        return float(sub)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq


ld = Loader()
s = '1, 2, 4, 52, 1'
res = ld.parse_format(s, Factory())
print(res)
