import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)

    app.setApplicationName("KakaoThemeViewer")
    app.setApplicationVersion("0.1.0")

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
