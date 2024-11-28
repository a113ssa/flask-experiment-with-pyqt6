import os
import sys

import requests  # type: ignore
from dotenv import load_dotenv  # type: ignore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

load_dotenv()

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Chatbot")

        layout = QVBoxLayout()

        response = self.retrieve_quest_response()
        layout.addWidget(self.set_label(response['questText']))

        mood = self.set_mood(response['mood'])
        mood.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(mood)

        buttons = self.set_variants(response['responseVariants'])
        for b in buttons:
            layout.addWidget(b)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_label(self, text):
        label = QLabel(self, text=text)
        font = label.font()
        font.setPointSize(15)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label.setFont(font)
        label.setMargin(20)

        return label

    def set_variants(self, variants: list[str]):
        buttons = []
        for item in variants:
            button = QPushButton(item)
            font = button.font()
            font.setPointSize(15)
            button.setFont(font)
            buttons.append(button)
        return buttons

    def set_mood(self, mood: str):
        label = QLabel()
        movie = QMovie('src/images/' + mood + '/1.gif')
        label.setMovie(movie)
        movie.start()

        return label

    def retrieve_quest_response(self):
        response = requests.get(os.environ['API_URL'] + '/chatbot').json()
        return response

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
