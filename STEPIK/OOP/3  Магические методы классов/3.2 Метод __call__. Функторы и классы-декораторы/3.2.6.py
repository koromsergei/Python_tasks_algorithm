class RenderList:
    def __init__(self, tag_list):
        self.tag_list = '<' + tag_list + '>'
        self.tag_list = '<ul>' if self.tag_list not in ('<ul>', '<ol>') else self.tag_list

    def __call__(self, *args, **kwargs):
        lst = args[0]
        print(self.tag_list)
        for i in lst:
            print(fr'<fi>{i}</li>')
        print(self.tag_list)


lst = ['obj1', 'obj2', 'obj3']
render = RenderList('ol')
ht = render(lst)
