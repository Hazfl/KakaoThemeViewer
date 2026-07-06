from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from core.theme_model import ThemeModel


class ChatPreview(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.theme: ThemeModel | None = None

        self.background = QLabel()
        self.background.setAlignment(Qt.AlignCenter)

        self.background.setScaledContents(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.background)

    def set_theme(self, theme: ThemeModel):

        self.theme = theme

        self.update_preview()

    def update_preview(self):

        self.background.clear()

        if self.theme is None:
            return

        image = self.find_background()

        if image is None:
            return

        pixmap = QPixmap(str(image.path))

        self.background.setPixmap(pixmap)

    def find_background(self):

        if self.theme is None:
            return None

        keywords = (
            "chatroom_bg",
            "chat_bg",
            "background",
        )

        for image in self.theme.images:

            name = image.name.lower()

            for keyword in keywords:

                if keyword in name:
                    return image

        return None
