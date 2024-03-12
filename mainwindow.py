import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QSizePolicy, QFrame

class Chessboard(QFrame):

        piece_images = {
            'Br': './pieces/Chess_rdt60.png',  # R pour la tour
            'Bn': './pieces/Chess_ndt60.png',  # N pour le cavalier
            'Bb': './pieces/Chess_bdt60.png',  # B pour le fou
            'Bq': './pieces/Chess_qdt60.png',  # Q pour la reine
            'Bk': './pieces/Chess_kdt60.png',  # K pour le roi
            'Bp': './pieces/Chess_pdt60.png',  # P pour le pion
        }

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chessboard')
        self.setFixedHeight(400)
        self.setFixedWidth(400)

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
                #square.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
