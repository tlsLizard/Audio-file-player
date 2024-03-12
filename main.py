import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Version 2 : Setting up a separate class
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buttun Holder App")

        button = QPushButton("Press me!")

        # Set up the button as our central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()