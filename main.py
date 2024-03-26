from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from toolbar import ToolBar
import sys
from seekSlider import SeekSlider

class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecteur audio")

        toolbar = ToolBar()
        self.addToolBar(toolbar)

        # Créer les boutons de contrôle
        self.playButton = QPushButton("Play")
        self.pauseButton = QPushButton("Pause")
        self.stopButton = QPushButton("Stop")
        self.slider = SeekSlider()


        # Connecter les boutons aux actions
        self.playButton.clicked.connect(self.slider.player.start)
        self.pauseButton.clicked.connect(self.slider.player.pause)
        self.stopButton.clicked.connect(self.slider.player.position)

        # Créer la mise en page
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.playButton)
        layoutH.addWidget(self.pauseButton)
        layoutH.addWidget(self.stopButton)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.slider)
        layoutV.addLayout(layoutH)

        central_widget = QWidget()
        central_widget.setLayout(layoutV)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec())
