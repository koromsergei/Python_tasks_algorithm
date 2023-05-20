from random import randint


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Router:
    buffer = {}

    def __init__(self):
        self.linked = {}

    def link(self, server):
        self.linked[server] = server.ip

    def unlink(self, server):
        self.linked.pop(server)

    def send_data(self):
        for i in self.linked.keys():
            i.data = [j for j in self.buffer if j.ip == self.linked[i]]


class Server:
    data = []

    def __init__(self):
        self.ip = randint(0, 100000)
        self.buffer = []

    def send_data(self, data: Data):
        Router.buffer[data] = data.ip

    def get_data(self):
        # подумать про очистку буфера
        return self.data

    def get_ip(self):
        return self.ip


router = Router()
sv_from = Server()
sv_from2 = Server()

router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
print(router.linked)

sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
print(router.buffer)

router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(sv_to.data)
print(sv_from.data)

# sv = Server()
# sv1 = Server()
# sv2 = Server()
#
# router = Router()
#
#
# print(sv.ip, sv1.ip)
