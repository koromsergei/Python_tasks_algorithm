class PhoneBook:
    def __init__(self):
        self.lst_numbers = []

    def add_phone(self, phone):
        self.lst_numbers.append(phone)

    def remove_phone(self, indx):
        self.lst_numbers.pop(indx)

    def get_phone_list(self):
        temp = {}
        for i in self.lst_numbers:
            temp[i.number] = i.fio
        return temp


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(8902138092, 'dfs fdsf ds'))
p.add_phone(PhoneNumber(123123421, 'dsf  f'))
print(p.get_phone_list())
