from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.theme_path: str | None = None

        self.setWindowTitle("Kakao Theme Viewer")
        self.resize(1400, 850)
        self.setMinimumSize(1000, 700)

        self._create_actions()
        self._create_menu()
        self._create_toolbar()
        self._create_statusbar()
        self._create_ui()

    # --------------------------------------------------
    # Actions
    # --------------------------------------------------

    def _create_actions(self) -> None:
        self.action_open = QAction("Open Theme...", self)
        self.action_open.triggered.connect(self.open_theme)

        self.action_reload = QAction("Reload", self)
        self.action_reload.triggered.connect(self.reload_theme)

        self.action_exit = QAction("Exit", self)
        self.action_exit.triggered.connect(self.close)

        self.action_about = QAction("About", self)
        self.action_about.triggered.connect(self.about)

    # --------------------------------------------------
    # Menu
    # --------------------------------------------------

    def _create_menu(self) -> None:
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.action_open)
        file_menu.addSeparator()
        file_menu.addAction(self.action_reload)
        file_menu.addSeparator()
        file_menu.addAction(self.action_exit)

        help_menu = self.menuBar().addMenu("&Help")
        help_menu.addAction(self.action_about)

    # --------------------------------------------------
    # Toolbar
    # --------------------------------------------------

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Toolbar")
        toolbar.setMovable(False)

        toolbar.addAction(self.action_open)
        toolbar.addAction(self.action_reload)

        self.addToolBar(toolbar)

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def _create_statusbar(self) -> None:
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Ready")

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    def _create_ui(self) -> None:
        central = QWidget()

        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Kakao Theme Viewer")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel{
                font-size:28px;
                font-weight:bold;
            }
        """)

        info = QLabel(
            "Open an Android KakaoTalk Theme Folder to preview it."
        )
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(info)
        layout.addStretch()

        self.setCentralWidget(central)

    # --------------------------------------------------
    # Slots
    # --------------------------------------------------

    def open_theme(self) -> None:
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Theme Folder",
        )

        if not folder:
            return

        self.theme_path = folder
        self.status.showMessage(folder)

    def reload_theme(self) -> None:
        if not self.theme_path:
            QMessageBox.information(
                self,
                "Reload",
                "No theme is currently opened.",
            )
            return

        self.status.showMessage(f"Reload : {self.theme_path}")

    def about(self) -> None:
        QMessageBox.about(
            self,
            "About",
            "Kakao Theme Viewer\nVersion 0.1.0",
        )
