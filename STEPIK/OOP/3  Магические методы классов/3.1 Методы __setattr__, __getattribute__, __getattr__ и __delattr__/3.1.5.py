class LessonItem:
    data_types = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if self.data_types[key] is type(value):
            super().__setattr__(key, value)

        else:
            raise TypeError()

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in('title', 'practise', 'duration'):
            super().__delattr__(item)


