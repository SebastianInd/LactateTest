from datetime import datetime, timedelta
from read_tcx import read_time_heart_rate
from test_specific_data import get_speed, get_measurement_times
from plot import plot

# Test settings
initial_speed = 13.0  # [km/h]
speed_increment = 1.0  # [km/h]
time_interval = timedelta(minutes=4)  # [min]
tcx_file = "lactate_test.tcx"  # Name of the TCX file produced in the lactate test
rpe = [8, 10, 12, 14, 15, 16]
lactate = [1.5, 1.5, 2.5, 2.1, 3.3, 5.4]

times, heart_rates = read_time_heart_rate(tcx_file)
speeds = get_speed(initial_speed, speed_increment, time_interval, times)
measurement_times = get_measurement_times(times, time_interval)

plot(times, measurement_times, heart_rates, speeds, rpe, lactate)
