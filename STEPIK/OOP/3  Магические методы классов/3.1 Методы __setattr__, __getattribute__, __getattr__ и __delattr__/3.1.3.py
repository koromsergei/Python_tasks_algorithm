class Book:
    def __init__(self, book='', author='', pages=0, year=0):
        self.book = book
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'book' or key == 'author':
            if type(value) == str:
                object.__setattr__(self, key, value)
            else:
                raise TypeError('TypeError')

        if key == 'pages' or key == 'year':
            if type(value) == int:
                object.__setattr__(self, key, value)
            else:
                raise TypeError('TypeError')


b = Book('Python', 'Van', 192, 2016)
print(b.book)
