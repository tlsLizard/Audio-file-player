import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Version 2 : Setting up a separate class
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QMainWindow()
        window.setWindowTitle('Chessboard')
        window.setGeometry(100, 100, 800, 800)

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()