from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QVBoxLayout,
    QWidget,
)


class ChatBubble(QFrame):

    def __init__(self, text: str, mine=False):

        super().__init__()

        if mine:
            color = "#FEE500"
            align = Qt.AlignRight
        else:
            color = "white"
            align = Qt.AlignLeft

        self.setStyleSheet(f"""
        QFrame{{
            background:{color};
            border-radius:12px;
            padding:8px;
        }}
        """)

        layout = QVBoxLayout(self)

        label = QLabel(text)
        label.setWordWrap(True)

        layout.addWidget(label)

        layout.setAlignment(align)


class PreviewPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        background:#A9BDCE;
        """)

        layout = QVBoxLayout(self)

        layout.setSpacing(12)

        title = QLabel("Preview")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        background:white;
        padding:8px;
        """)

        layout.addWidget(title)

        layout.addSpacing(15)

        layout.addWidget(ChatBubble("안녕하세요!"))
        layout.addWidget(ChatBubble("카카오톡 테마 미리보기입니다."))

        layout.addWidget(
            ChatBubble(
                "아직 CSS는 적용되지 않았습니다.",
                True
            )
        )

        layout.addStretch()

    def apply_background(self, color: str):

        self.setStyleSheet(f"""
        background:{color};
        """)
