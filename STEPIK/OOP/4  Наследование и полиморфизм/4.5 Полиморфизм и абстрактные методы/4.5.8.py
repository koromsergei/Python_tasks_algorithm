from abc import abstractmethod, ABC


class CountryInterface(ABC):
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, value):
        self._name = value

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_info(self):
        print(self._name, 'country')


n = Country('Russia')
n.get_info()
print(n.name)
