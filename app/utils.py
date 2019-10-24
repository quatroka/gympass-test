from datetime import datetime, timedelta


def parse_time(time):
    return datetime.strptime(time, '%H:%M:%S.%f').time()


def parse_lap_time(lap_time):
    time = datetime.strptime(lap_time, '%M:%S.%f').time()
    return timedelta(hours=time.hour, minutes=time.minute,
                     seconds=time.second, microseconds=time.microsecond)
