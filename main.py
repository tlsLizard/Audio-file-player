from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from toolbar import ToolBar
import sys

class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecteur audio")

        toolbar = ToolBar()
        
        self.addToolBar(toolbar)

        # Créer le lecteur multimédia
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)


        # Créer les boutons de contrôle
        self.playButton = QPushButton("Play")
        self.pauseButton = QPushButton("Pause")
        self.stopButton = QPushButton("Stop")

        self.playButton.clicked.connect(self.player.play)
        self.pauseButton.clicked.connect(self.player.pause)
        self.stopButton.clicked.connect(self.player.stop)

        # Créer la mise en page
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.playButton)
        layoutH.addWidget(self.pauseButton)
        layoutH.addWidget(self.stopButton)

        layoutV = QVBoxLayout()
        # layoutV.addWidget(self.player)
        layoutV.addLayout(layoutH)

        central_widget = QWidget()
        central_widget.setLayout(layoutV)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec())
