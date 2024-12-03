import os
import random
import sys
from functools import partial

import i18n  # type: ignore
import requests  # type: ignore
from dotenv import load_dotenv  # type: ignore
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

load_dotenv()
i18n.load_path.append('src/locales')
i18n.set('locale', os.environ['LOCALE'])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Quest Adventure")
        self.set_hello_screen()
        self.resize(800, 600)

    def set_hello_screen(self):
        layout = QVBoxLayout()

        hello_label = self.set_game_quest_label(i18n.t('game.hello'), alignment=Qt.AlignmentFlag.AlignCenter)
        start_label = self.set_game_quest_label(i18n.t('game.start_game'), font_size=18, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(hello_label)
        layout.addWidget(start_label)

        button = self.set_game_button(i18n.t('game.confirm'), 25)
        button.clicked.connect(self.start_game)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.set_background_color(widget, Qt.GlobalColor.black, Qt.GlobalColor.lightGray)
        self.setCentralWidget(widget)

    def start_game(self):
        response = self.retrieve_quest_response()
        self.set_game_screen(response)

    def set_font(self, font_size: int, label: QLabel | QPushButton):
        font = label.font()
        font.setPointSize(font_size)
        label.setFont(font)

    def set_background_color(self, widget: QWidget, color: Qt.GlobalColor, font_color: Qt.GlobalColor):
        palette = widget.palette()
        palette.setColor(widget.backgroundRole(), color)
        palette.setColor(widget.foregroundRole(), font_color)
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

    def set_game_screen(self, response: dict):
        layout = QVBoxLayout()

        layout.addWidget(self.set_game_quest_label(response['questText'], margin=10))

        mood = self.set_game_mood(response['mood'])
        mood.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(mood)

        buttons = self.set_game_variants(response['responseVariants'])
        for b in buttons:
            layout.addWidget(b)

        widget = QWidget()
        widget.setLayout(layout)

        self.set_background_color(widget, Qt.GlobalColor.black, Qt.GlobalColor.lightGray)
        self.setCentralWidget(widget)

    def set_game_quest_label(self, text: str, font_size: int=15, margin: int=20, word_wrap: bool=True, alignment: Qt.AlignmentFlag=Qt.AlignmentFlag.AlignLeft) -> QLabel:
        label = QLabel(text)
        self.set_font(font_size, label)
        label.setWordWrap(word_wrap)
        label.setAlignment(alignment)
        label.setMargin(margin)
        return label

    def set_game_button(self, text: str, font_size: int) -> QPushButton:
        button = QPushButton(text)
        self.set_font(font_size, button)
        return button

    def set_game_variants(self, variants: list[str]) -> list[QPushButton]:
        buttons = []
        for item in variants:
            button = self.set_game_button(item, 20)
            button.released.connect(partial(self.set_next_quest, item))
            buttons.append(button)
        return buttons

    def set_next_quest(self, message: str):
        response = self.send_message(message)
        self.set_game_screen(response)

    def set_game_mood(self, mood: str) -> QLabel:
        label = QLabel()
        mood_index = random.randint(1, 3)
        movie = QtGui.QMovie('src/images/' + mood + f"/{mood_index}.gif")
        label.setMovie(movie)
        label.setMinimumHeight(200)
        movie.start()

        return label

    def retrieve_quest_response(self) -> dict:
        response = requests.get(os.environ['API_URL'] + '/chatbot')
        return response.json()

    def send_message(self, message: str) -> dict:
        print('MESSAGE: ' + message)
        response = requests.post(os.environ['API_URL'] + '/chatbot', json={'message': message})
        return response.json()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
