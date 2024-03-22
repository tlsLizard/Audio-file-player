from PySide6.QtWidgets import QToolBar
from PySide6.QtCore import Qt
from fileSelector import FileSelector

class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.addAction("Ouvrir un fichier", self.open_file)
        self.addAction("Ajouter un dossier", self.open_folder)
        self.setMovable(False)
        self.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)

    def open_file(self):
        return FileSelector("file")

    def open_folder(self):
        return FileSelector("folder")