filename = ['boat.jpg',
            'web.png',
            'text.png',
            'python.doc',
            'ava.8.jpg',
            'data.html',
            'text.txt',
            'forest.jpeg'
            ]


class ImageFileAcceptor:
    def __init__(self, extension: tuple):
        self.extension = extension

    def __call__(self, *args, **kwargs):
        file_name = args[0][::-1].split('.')
        if file_name[0][::-1] in self.extension:
            print(file_name[0][::-1])
            return True
        return False


acc = ImageFileAcceptor(('txt', 'jpg'))
print(list(filter(acc, filename)))
