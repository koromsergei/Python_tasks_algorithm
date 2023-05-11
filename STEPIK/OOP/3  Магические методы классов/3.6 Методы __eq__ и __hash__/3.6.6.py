class ShopItem:
    def __init__(self, name: str, weight: (int, float), price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst = [ShopItem('Системный блок', 213, 233),
       ShopItem('Монитор', 2222, 213.2),
       ShopItem('Клавиатура', 2222, 213.2),
       ShopItem('Монитор', 2222, 213.2)]

print(lst[1] == lst[3])
shop_dic = {}
val = 0
for i in lst:
    shop_dic[i] = [i, val]
shop_dic = {i: [i, ] for i in lst}
