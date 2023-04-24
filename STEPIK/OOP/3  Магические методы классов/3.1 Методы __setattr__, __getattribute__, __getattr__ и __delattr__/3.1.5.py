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
        if item not in ('title', 'practise', 'duration'):
            super().__delattr__(item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem):
        self.lessons.append(lesson)

    def remove_lesson(self, index):
        self.lessons.pop(index)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module: Module):
        self.modules.append(module)

    def remove_module(self, index):
        self.modules.pop(index)


course = Course('Python OOP')
module_1 = Module('part 1')
module_1.add_lesson(LessonItem('lesson 1', 7, 1000))
module_1.add_lesson(LessonItem('lesson 2', 12, 900))
module_1.add_lesson(LessonItem('lesson 3', 3, 800))

course.add_module(module_1)

print(course.modules)
lan = LessonItem('lesson 1', 7, 1000)
del lan.title
print(lan.title)