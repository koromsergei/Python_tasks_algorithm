import numpy as np


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track_lines = ()

    def add_track(self, tr):
        self.track_lines = (*self.track_lines, tr)

    def get_track(self):
        return self.track_lines

    @classmethod
    def _verify(cls, other):
        if not type(other) == Track:
            raise ValueError
        return True

    def __len__(self):
        length_1 = 0
        if self._verify(self):
            for i in self.get_track():
                length_1 += np.sqrt(pow(i.to_x, 2) + pow(i.to_y, 2))
        return int(length_1)

    def __eq__(self, other):
        print(len(self))
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)


tr1 = Track(0, 0)
tr1.add_track(TrackLine(1, 2, 100))
tr1.add_track(TrackLine(3, 4, 100))
tr1.add_track(TrackLine(5, 44, 100))

tr2 = Track(0, 0)
tr2.add_track(TrackLine(1, 2, 100))
tr2.add_track(TrackLine(3, 4, 100))
tr2.add_track(TrackLine(5, 44, 100))
print(tr1 == tr2)
print(tr1 > tr2)
