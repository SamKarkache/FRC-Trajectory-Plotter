import pandas as pd
import matplotlib.pyplot as plt
import csv


def plot_trajectory(log_path: str):
    x = []
    y = []
    with open(log_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[1] == "DriveTrajectory" and row[2] != "Start" and row[2] != "Finish":
                x.append(float(row[6]))
                y.append(float(row[8]))

    if len(x) == 0 or len(y) == 0:
        raise Exception(f'No Drive Trajectory data found in {log_path}')

    plt.plot(x, y)
    plt.title(f'Trajectory Path for {log_path}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.savefig(f'static/images/output.png')


if __name__ == "__main__":
    plot_trajectory("logfile.csv")
