"""
This is where it all begins starts up the voting station
"""

from PyQt6.QtWidgets import QApplication
from gui import MainWindow
import sys
import os

def clear_votes_file() -> None:
    """
    This is where it becomes a clean slate by clearing everything in the CSV file I used ChatGPT for this because I couldn't figure out how to clean itself out it was the simplest thing
    :return:None
    """
    with open("votes.csv", "w") as file:
        file.write("")  # This discards everything this line couldn't figure this out for the longest time

def main() -> None:

    """
    Pulls up the PyQt6 Window
    :return:None
    """
    clear_votes_file()  # This wipes it clean before a new run

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
