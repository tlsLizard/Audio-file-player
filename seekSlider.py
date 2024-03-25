import sys
from PySide6.QtWidgets import QSlider, QApplication, QMainWindow
from PySide6.QtCore import Qt, Slot
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
import time


class AudioPlayerThread(Thread):
    def __init__(self, audio : AudioSegment):
        super().__init__()
        self.audio = audio
        self.percent : int = 1
        self.start_time : int = 0
        self.number_of_minutes : int = 0
        self.remaining_seconds : int = 0
        
    def run(self):
        player : Thread = Thread(target=play, args=(self.audio,))

        player.name = "AudioPlayerThread"

        self.start_time = time.time()

        player.start()

    def getCurrentTime(self) -> int:
        current_time = round(time.time() - self.start_time)

        # Convertir les secondes en minutes
        self.number_of_minutes = current_time // 60

        # Calculer les secondes restantes
        self.remaining_seconds = current_time % 60

        # Retourner le temps écoulé en secondes
        return self.number_of_minutes * 60 + self.remaining_seconds
    
    def getPercent(self) -> int:
        self.percent = round((self.getCurrentTime() / self.audio.duration_seconds) * 100)
        return self.percent

class SeekSlider(QSlider):

    def __init__(self):
        super().__init__()

        audio : AudioSegment = AudioSegment.from_file("/home/xelame/Music/Fuji Kaze/michi-teyu-ku-overflowing-official-video.wav")

        self.player = AudioPlayerThread(audio)

        self.player.run()

        self.setRange(0, 100)
        self.setValue(0)
        self.setTickInterval(100)

        self.setOrientation(Qt.Orientation.Horizontal)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    seekSlider = SeekSlider()
    window.setCentralWidget(seekSlider)
    window.show()
    sys.exit(app.exec())
