# Signals and slots are used for communication between widgets
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()  # required to avoid bugs
def say_hello():
    print("Button Clicked, Hello!")


app = QApplication(sys.argv)

button = QPushButton("Click Me")

button.clicked.connect(say_hello)

button.show()

app.exec()
