from PySide6.QtWidgets import QToolBar
from PySide6.QtCore import Qt
from fileSelector import FileSelector

class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.addAction("Ouvrir un fichier", FileSelector.open_file)
        self.addAction("Ajouter un dossier", FileSelector.open_folder)
        self.setMovable(False)
        self.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)