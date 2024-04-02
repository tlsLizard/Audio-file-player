from PySide6.QtWidgets import QSlider, QApplication, QMainWindow
from pydub import AudioSegment
from PySide6.QtCore import Qt, Slot, QTimer
import pyaudio
import wave
import sys
import time

class SeekSlider(QSlider):

    def __init__(self):
        super().__init__()

        self.audio : AudioSegment = AudioSegment.from_file("/home/xelame/Music/Fuji Kaze/michi-teyu-ku-overflowing-official-video.wav")

        # Exporter le fichier MP3 en WAV
        self.audio.export('output.wav', format='wav')

        self.wf = wave.open('output.wav', 'rb')

        # Instantiate PyAudio and initialize PortAudio system resources (2)
        p = pyaudio.PyAudio()

        # Open stream using callback (3)
        self._stream = p.open(format=p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True,
                        stream_callback=self._callback)

        self.setRange(0, 100)
        self.setValue(0)
        self.setTickInterval(100)

        self.setOrientation(Qt.Orientation.Horizontal)

        self._current_time = time.time()

        # Créer un temporisateur pour mettre à jour la position de lecture régulièrement
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_slider_position())
        self.timer.start(100)  # Mettre à jour toutes les 100 millisecondes

    def _callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        self.update_slider_position()
        return (data, pyaudio.paContinue)
    
    def pause(self):
        if not self._stream.is_stopped():
            self._stream.stop_stream()

    def start(self):
        if self._stream.is_stopped():
            self._stream.start_stream()
    
    def update_slider_position(self):
        # Mettre à jour la position du curseur en fonction de la position de lecture
        position = self._stream.get_time() - self._current_time
        value = int(position / self.audio.duration_seconds * self.maximum())
        print("Position : ", position, " audio.lenght : ", self.audio.duration_seconds,  " max : ", self.maximum(), " value : ", value)
        self.setValue(value)
        self.setSliderPosition(value)

    @Slot(int)
    def position(self):
        return self.wf.tell()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    seekSlider = SeekSlider()
    window.setCentralWidget(seekSlider)
    window.show()
    sys.exit(app.exec())
