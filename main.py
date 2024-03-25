from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QSlider
from PySide6.QtMultimedia import QAudioOutput
from PySide6.QtCore import Qt
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

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.playButton)
        layoutH.addWidget(self.pauseButton)
        layoutH.addWidget(self.stopButton)

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
