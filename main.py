from datetime import timedelta
from read_tcx import read_time_heart_rate
from test_specific_data import get_speed, get_measurement_times
from plot import plot

# Test settings
initial_speed = 11.0  # [km/h]
time_interval = timedelta(minutes=5)  # [min]
speed_increment = 1.0  # [km/h]
basal_measurement = True  # [bool]
end_measurement = True  # [bool]
tcx_file = "lactate_test.tcx"  # [string]

# Test measurements
rpe = [6, 10, 11, 12, 14, 16, 17, 19, 20]
lactate = [1.5, 3.9, 1.4, 1.8, 1.3, 2.3, 5.3, 8.9, 9.8]

# Process data and plot
times, heart_rates = read_time_heart_rate(tcx_file)
speeds = get_speed(initial_speed, speed_increment, time_interval, times)
measurement_times = get_measurement_times(
    times, time_interval, basal_measurement, end_measurement
)

plot(times, measurement_times, heart_rates, speeds, rpe, lactate)
