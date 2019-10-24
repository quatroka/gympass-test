class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.laps = []

    def final_time(self):
        return sorted(self.laps, key=lambda lap: lap.time)[-1].time

    def laps_total_time(self):
        return sum(self.laps).lap_time

    def best_lap(self):
        return min(self.laps).lap_time

    def average_speed_in_race(self):
        return sum(list(map(lambda lap: lap.average_speed, self.laps))) / len(
            self.laps)

    def __repr__(self):
        return f'<Driver id={self.id} name={self.name}>'

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
