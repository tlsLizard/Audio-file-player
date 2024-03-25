from PySide6.QtWidgets import QSlider, QApplication, QMainWindow
from PySide6.QtCore import Qt
from pydub import AudioSegment
from pydub.playback import play
import sys
from threading import Thread
import time

class AudioPlayerThread(Thread):
    def __init__(self, audio : AudioSegment):
        super().__init__()
        self.audio = audio
        self.percent : int = 1

    def run(self):
        player : Thread = Thread(target=play, args=(self.audio,))

        player.start()

        while player.is_alive():
            time.sleep(self.audio.duration_seconds / 100)
            timePlayed = self.audio.duration_seconds / 100 * self.percent
            print( str(self.percent) + " %")
            self.percent += 1

        player.join()


class SeekSlider(QSlider):


    def __init__(self):
        super().__init__()

        audio : AudioSegment = AudioSegment.from_file("/home/xelame/Music/Fuji Kaze/michi-teyu-ku-overflowing-official-video.wav")

        player : Thread = AudioPlayerThread(audio)

        player.start()

        self.setRange(0, 100)
        self.setValue(0)
        self.setTickInterval(100 / audio.duration_seconds)

        self.setOrientation(Qt.Orientation.Horizontal)


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setCentralWidget(SeekSlider())
    window.show()
    sys.exit(app.exec())
