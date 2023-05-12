from datetime import datetime, timedelta
from typing import List


def get_speed(
    initial_speed: float,
    speed_increment: float,
    time_interval: timedelta,
    times: List[datetime],
) -> list:
    speeds = []
    start_time = times[0]
    for time in times:
        delta_time = time - start_time
        interval = delta_time.total_seconds() // time_interval.total_seconds()
        current_speed = initial_speed + interval * speed_increment
        speeds.append(current_speed)
    return speeds


def get_measurement_times(times: List[datetime], time_interval: timedelta):
    measurement_times = []
    measurement_time = times[0] + time_interval
    while measurement_time < times[-1]:
        measurement_times.append(measurement_time)
        measurement_time += time_interval
    return measurement_times
