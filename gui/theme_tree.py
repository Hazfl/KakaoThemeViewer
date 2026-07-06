from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
)


class ThemeTree(QTreeWidget):
    """
    좌측 테마 파일 트리
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setHeaderLabels(["Theme Files"])
        self.setColumnCount(1)

        self.setAnimated(True)
        self.setIndentation(18)

    def clear_theme(self):
        self.clear()

    def load_theme(self, folder: str):

        self.clear()

        root = Path(folder)

        root_item = QTreeWidgetItem([root.name])
        root_item.setExpanded(True)

        self.addTopLevelItem(root_item)

        self._scan(root, root_item)

    def _scan(self, directory: Path, parent: QTreeWidgetItem):

        entries = sorted(
            directory.iterdir(),
            key=lambda x: (x.is_file(), x.name.lower())
        )

        for entry in entries:

            item = QTreeWidgetItem([entry.name])

            if entry.is_dir():

                item.setExpanded(False)

                parent.addChild(item)

                self._scan(entry, item)

            else:

                parent.addChild(item)
