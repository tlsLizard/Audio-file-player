import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QSizePolicy, QFrame

class Chessboard(QFrame):
    def __init__(self, parent):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(0, 0, 0, 0)

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.draw_squares()
        self.setLayout(self.layout)
        self.show()

    def draw_squares(self):
        for row, rank in enumerate('87654321'):
            for col, file in enumerate('abcdefgh'):
                square = QWidget(self)
                square.setObjectName(file + rank)
                square.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                if row % 2 == col % 2:
                    square.setStyleSheet('background-color: #F0D9B5')
                else:
                    square.setStyleSheet('background-color: #B58863')
                self.layout.addWidget(square, row, col)

def main():
    app = QApplication(sys.argv)
    window = Chessboard()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
