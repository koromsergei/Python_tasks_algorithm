class Money:
    def __init__(self, money):
        self.__money = money if self.__check_money(money) else 0

    @staticmethod
    def __check_money(money):
        return money >= 0

    def set_money(self, money):
        self.__money = money if self.__check_money(money) else self.__money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money


mn_1 = Money(-1)
mn_2 = Money(10)

mn_1.set_money(100)
mn_2.add_money(mn_1)

print(mn_1.get_money())
print(mn_2.get_money())


