import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv) # [] can be used too
label = QLabel("Hello World!")
label.show()
# Note that this creates two applications....
label2 = QLabel("<font color=red size=40>Hello World!</font>")
label2.show()
app.exec()

