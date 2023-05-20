class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        print('Post method', request)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods=methods)

    def render_request(self, request, method: str):
        if method in self.methods:
            a = getattr(self, method.lower())
            a(request)
        else:
            raise TypeError('Not valid')


dv = DetailView()
print(dv.methods)
dv1 = DetailView(methods=('PUT', 'POST'))
dv.render_request('asd', 'GET')


