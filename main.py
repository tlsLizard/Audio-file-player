from PySide6.QtWidgets import QApplication, QFileDialog
from pydub import AudioSegment
from pydub.playback import play

# Créer une application Qt
app = QApplication([])

# Afficher la boîte de dialogue pour sélectionner un fichier
fichier_selectionne, _ = QFileDialog.getOpenFileName(None, "Sélectionner un fichier MP3", "", "Fichiers MP3 (*.mp3)")

# Vérifier si un fichier a été sélectionné
if fichier_selectionne:
    print("Fichier sélectionné :", fichier_selectionne)

    audio = AudioSegment.from_file(fichier_selectionne, format="mp3")

    play(audio)

else:
    print("Aucun fichier sélectionné.")