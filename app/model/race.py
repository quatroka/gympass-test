from collections import namedtuple

from app.model.driver import Driver
from app.model.lap import Lap
from app.utils import parse_lap_time, parse_time


class Race:
    DEFAULT_FILE_NAME = 'race_log.txt'

    def __init__(self):
        self.drivers = []
        self.race_data = []

    def load_race_log(self, file_name=DEFAULT_FILE_NAME):
        with open(file_name, 'r') as file:
            data = file.readlines()
            if data and 'Hora' in data[0]:
                self.race_data = data[1:]
                return
            self.race_data = data

    def build_race_history_from_log(self):
        drivers = {}
        RowData = namedtuple('RowData',
                             'time driver_id driver_name lap_number lap_time '
                             'average_speed')
        for line in self.race_data:
            cleaned_line = self.__clean_line(line)
            row_data = RowData(*cleaned_line)

            driver = Driver(row_data.driver_id, row_data.driver_name)
            if driver.id not in drivers.keys():
                drivers[driver.id] = driver

            lap = Lap(row_data.lap_number, parse_lap_time(row_data.lap_time),
                      parse_time(row_data.time),
                      float(row_data.average_speed.replace(',', '.')))

            drivers[driver.id].laps.append(lap)
        self.drivers = list(drivers.values())

    @staticmethod
    def __clean_line(line):
        striped_line = ' '.join(line.split()).strip().split()
        striped_line.remove('–')
        return striped_line

    def race_curiosities(self):
        drivers_laps_total_time = list(
            map(lambda driver: driver.best_lap(), self.drivers))
        print(f'Best in the race lap: {min(drivers_laps_total_time)}')

    def scoreboard(self):
        print('-' * 155)
        print('{:<20s}{:<12s}{:<16s}{:<16s}{:<18s}{:<18}{:<18}{:<12}'.format(
            'Finish Position',
            'Driver ID',
            'Driver Name',
            'Number of Laps',
            'Best Lap',
            'Total Race Time',
            'Averange Speed',
            'Difference time from first driver'
        ))
        print('-' * 155)

        sorted_drivers_by_total_race_time = sorted(self.drivers, key=lambda
            driver: driver.final_time())
        for index, driver in enumerate(sorted_drivers_by_total_race_time):
            print(
                '{:<20s}{:<12s}{:<16s}{:<16s}{:<18s}{:<18}{:<18}{:<12}'.format(
                    str(index + 1),
                    driver.id,
                    driver.name,
                    str(len(driver.laps)),
                    str(driver.best_lap()),
                    str(driver.laps_total_time()),
                    str(round(driver.average_speed_in_race(), 3)),
                    '-' + str(driver.laps_total_time() -
                              sorted_drivers_by_total_race_time[
                                  0].laps_total_time())
                ))
        print('-' * 155)
