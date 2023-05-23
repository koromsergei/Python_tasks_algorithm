class Aircraft:
    def __init__(self, model: str, mass: int, speed: int, top: int):
        self.model = model if type(model) is str else None
        self.mass = mass if type(mass) is int else None
        self.speed = speed if type(speed) is int else None
        self.top = top if type(top) is int else None
        for i in self.__dict__.values():
            if i is None:
                raise TypeError


class PassengerAircraft(Aircraft):
    def __init__(self, model: str, mass: int, speed: int, top: int, chairs: int):
        if type(chairs) is not str:
            raise TypeError
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model: str, mass: int, speed: int, top: int, weapons: int):
        if type(weapons) is not str:
            raise TypeError
        super().__init__(model, mass, speed, top)
        self._weapons = weapons





