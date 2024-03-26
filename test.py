import pydub
import pyaudio
import time
import wave
import os

# Charger le fichier MP3
audio : pydub.AudioSegment = pydub.AudioSegment.from_mp3('/home/xelame/Music/guerrier-clip-officiel.mp3')


# Exporter le fichier MP3 en WAV
audio.export('output.wav', format='wav')

wf = wave.open('output.wav', 'rb')

# Define callback for playback (1)
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    # If len(data) is less than requested frame_count, PyAudio automatically
    # assumes the stream is finished, and the stream stops.
    return (data, pyaudio.paContinue)

# Instantiate PyAudio and initialize PortAudio system resources (2)
p = pyaudio.PyAudio()

# Open stream using callback (3)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

# Démarrer la lecture
current_position = 0
stream.start_stream()

# Attendre un certain temps
time.sleep(1000)

# Mettre en pause la lecture
stream.stop_stream()

# Attendre un certain temps
time.sleep(2)


# Reprendre la lecture à partir de la position actuelle
stream.start_stream()

# Libérer les ressources PyAudio
stream.stop_stream()
stream.close()
p.terminate()

os.remove('output.wav')
