import sys
import argparse
import pandas as pd

from PySide6.QtCore import QDateTime, QTimeZone
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from main_widget import Widget


def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)
    df = df.sort_values(["mag"])
    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)


    # My local timezone
    timezone = QTimeZone(b"Europe/Berlin")

    # Get timestamp transformed to our timezone
    df["time"] = df["time"].apply(lambda x: transform_date(x, timezone))
    df = df.sort_values(["time"])
    magnitudes = df["mag"]
    times = df["time"]
    return times, magnitudes


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)

    # Qt Application
    app = QApplication(sys.argv)

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec())