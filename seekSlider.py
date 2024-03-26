from PySide6.QtWidgets import QSlider, QApplication, QMainWindow
from pydub import AudioSegment
from PySide6.QtCore import Qt, Slot
import pyaudio
import wave
import sys

class SeekSlider(QSlider):

    def __init__(self):
        super().__init__()

        audio : AudioSegment = AudioSegment.from_file("/home/xelame/Music/Fuji Kaze/michi-teyu-ku-overflowing-official-video.wav")

        # Exporter le fichier MP3 en WAV
        audio.export('output.wav', format='wav')

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

    def _callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        print("Hello")
        return (data, pyaudio.paContinue)
    
    def pause(self):
        if not self._stream.is_stopped():
            self._stream.stop_stream()

    def start(self):
        if self._stream.is_stopped():
            self._stream.start_stream()
    
    def update_slider_position(self):
        # Mettre à jour la position du curseur en fonction de la position de lecture
        position = self.stream.get_time()
        value = int(position / len(self.audio) * self.maximum())
        self.setValue(value)

    @Slot(int)
    def position(self):
        return print(self.wf.tell())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    seekSlider = SeekSlider()
    window.setCentralWidget(seekSlider)
    window.show()
    sys.exit(app.exec())
