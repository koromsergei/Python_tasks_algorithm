class HandlerGET:
    def __init__(self, methods=('GET',)):

        self.methods = methods

    def __call__(self, func):
        def wrapper(request: dict, *args, **kwargs):
            self.request_dict = request['method']
            if self.request_dict in self.methods:
                if self.request_dict is None or self.request_dict == 'GET':
                    return self.get(func, request)
                elif self.request_dict == 'POST':
                    return self.post(func, request)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET:{func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST:{func(request)}'


@HandlerGET(methods=('GET', 'POST'))
def contact(request: dict):
    return 'Smt'


res = contact({'method': 'GET', 'url': 'contact.html'})
print(res)
