class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_bs = [BookStudy('Python', 'B', 2020),
          BookStudy('Python', 'B', 2021),
          BookStudy('Java', 'B', 2019),
          BookStudy('Python', 'B', 2000)]


unique_books = 0

print([hash(i) for i in lst_bs])
print(len(set([hash(i) for i in lst_bs])))
