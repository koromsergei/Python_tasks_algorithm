from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper()
    CHARS_FOR_NUMBERS = digits

    @classmethod
    def check_card_number(cls, number: str):
        count = 0
        for i in number.split('-'):
            if int(i) // 1000 > 9 or not (set(i).issubset(set(cls.CHARS_FOR_NUMBERS))):
                raise ValueError("некорректное поле number")
            count += 1
        if count == 4:
            return True
        else:
            raise ValueError("некорректное поле number")

    @classmethod
    def check_name(cls, name: str):
        count = 0
        for i in name.split():
            if not (set(i).issubset(set(cls.CHARS_FOR_NAME))):
                raise ValueError("некорректное поле name")
            count += 1
        if count == 2:
            return True
        else:
            raise ValueError("некорректное поле name")


is_name = CardCheck.check_name('SERGEI KOROMYSLOV')
is_number = CardCheck.check_card_number('1234-1231-1234-1234')
