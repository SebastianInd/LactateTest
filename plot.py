import matplotlib.pyplot as plt
from datetime import datetime
from typing import List


def plot(
    times: List[datetime],
    measurement_times: List[datetime],
    heart_rates: List[int],
    speeds: List[float],
    rpe: List[int],
    lactate: List[float],
):
    # Create figure and subplots
    fig, ax1 = plt.subplots()

    # Plot heart rate measurements
    ax1.plot(times, heart_rates, "r-")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Heart Rate (bpm)")
    ax1.set_ylim(0.0, 225.0)
    ax1.yaxis.grid(True, linestyle="--", linewidth=0.5)

    # Plot speed measurements
    ax2 = ax1.twinx()
    ax2.plot(times, speeds, "y-")
    ax2.set_ylabel("Speed (km/h)")
    ax2.set_ylim(6.0, 20.0)

    # Plot RPE measurements
    ax3 = ax1.twinx()
    ax3.plot(measurement_times, rpe, "b.:")
    ax3.set_ylim(0.0, 20.0)
    ax3.set_yticklabels([])
    ax3.get_yaxis().set_tick_params(length=0)
    for i, j in zip(measurement_times, rpe):
        ax3.annotate(str(j), xy=(i, j))

    # Plot lactate measurements
    ax4 = ax1.twinx()
    ax4.plot(measurement_times, lactate, "gD:")
    ax4.set_ylim(-1.0, 10.0)
    ax4.set_yticklabels([])
    ax4.get_yaxis().set_tick_params(length=0)
    for i, j in zip(measurement_times, lactate):
        ax4.annotate(str(j), xy=(i, j))

    # Display the plot
    plt.show()
