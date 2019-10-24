class Lap:
    def __init__(self, lap_number=None, lap_time=None, time=None,
                 average_speed=None):
        self.lap_number = lap_number
        self.lap_time = lap_time
        self.time = time
        self.average_speed = average_speed

    def __lt__(self, other):
        return self.lap_time < other.lap_time

    def __sub__(self, other):
        return Lap(lap_time=self.lap_time - other.lap_time)

    def __add__(self, other):
        return Lap(lap_time=self.lap_time + other.lap_time)

    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

    def __eq__(self, other):
        return self.lap_number == other.lap_number

    def __hash__(self):
        return hash(self.lap_number)
