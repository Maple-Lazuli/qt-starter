import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import QObject, Signal, Slot


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # Create Widgets
        self.edit = QLineEdit("Write my name Here.....")
        self.button = QPushButton("Show Greetings")
        self.button.clicked.connect(self.greetings)
        # Create a layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
