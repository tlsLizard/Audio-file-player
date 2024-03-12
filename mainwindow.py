import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PySide6.QtCore import Qt

class Chessboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chessboard')
        self.setGeometry(100, 100, 400, 400)

        grid = QGridLayout()
        self.setLayout(grid)

        # Création des cases de l'échiquier
        for i in range(8):
            for j in range(8):
                label = QBut
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet('background-color: {};'.format('white' if (i + j) % 2 == 0 else 'gray'))
                grid.addWidget(label, i, j)

        self.show()

def main():
    app = QApplication(sys.argv)
    window = Chessboard()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
