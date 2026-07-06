from __future__ import annotations

from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QSplitter,
)

from PySide6.QtCore import Qt

from gui.theme_tree import ThemeTree
from gui.preview_panel import PreviewPanel
from gui.property_panel import PropertyPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kakao Theme Viewer")

        self.resize(1600, 900)

        self.theme_path = None

        self.create_ui()

    def create_ui(self):

        splitter = QSplitter()

        splitter.setOrientation(Qt.Horizontal)

        self.tree = ThemeTree()

        self.preview = PreviewPanel()

        self.properties = PropertyPanel()

        splitter.addWidget(self.tree)
        splitter.addWidget(self.preview)
        splitter.addWidget(self.properties)

        splitter.setSizes([300, 900, 350])

        self.setCentralWidget(splitter)

    def open_theme(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Theme Folder"
        )

        if not folder:
            return

        self.theme_path = folder

        self.tree.load_theme(folder)

    def reload_theme(self):

        if self.theme_path is None:

            QMessageBox.information(
                self,
                "Reload",
                "No Theme Loaded."
            )

            return

        self.tree.load_theme(self.theme_path)
