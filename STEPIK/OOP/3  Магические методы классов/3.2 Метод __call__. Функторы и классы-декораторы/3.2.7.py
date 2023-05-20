class HandlerGET:
    def __init__(self, func):
        self.__func = func
        self.request_dict = None

    def __call__(self, request: dict, *args, **kwargs):
        self.request_dict = request
        method = 'GET' if request['method'] is None else request['method']
        if method != 'GET':
            return None
        data_str = f'{method}:<{self.__func(request)}>'
        return data_str

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func()}'


@HandlerGET
def contact(request: dict):
    return 'Smt'


res = contact({'method': 'GET', 'url': 'contact.html'})
print(res)

