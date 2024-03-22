from PySide6.QtWidgets import QFileDialog

class FileSelector(QFileDialog):
    def __init__(self, type):
        super().__init__()

        self.type = type

        if self.type == "file":
            self.setFileMode(QFileDialog.FileMode.ExistingFile)
            self.setNameFilter("Fichiers audio (*.mp3 *.wav)")
        if self.type == "folder":
            self.setFileMode(QFileDialog.FileMode.Directory)

        if self.exec() == QFileDialog.DialogCode.Accepted:
            selected_files = self.selectedFiles()
            print("Fichiers sélectionnés:", selected_files)
        else:
            print("Aucun fichier sélectionné")


        