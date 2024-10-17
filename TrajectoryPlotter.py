import pandas as pd
import matplotlib.pyplot as plt
import csv

from IPython.core.pylabtools import figsize

# TODO: Ability to input points (ex. barrels)
# TODO: Underlay field image
# TODO: Show the outline of the robot based on inputted robot dimensions
# TODO: The angle of the robot should be the same as the angle in log file
# TODO: add units, be able to swap units

def plot_trajectory(log_path: str):
    x = []
    y = []
    with open(log_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                if row[1] == "DriveTrajectory" and row[2] != "Start" and row[2] != "Finish":
                    x.append(float(row[6]))
                    y.append(float(row[8]))
            except IndexError:
                continue

    if len(x) == 0 or len(y) == 0:
        raise Exception(f'No Drive Trajectory data found in {log_path}')

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y)
    plt.title(f'Trajectory Path for {log_path}')
    plt.xlim(0, 9.144)
    plt.ylim(0, 9.144 / 2)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.savefig(f'static/images/output.png')
