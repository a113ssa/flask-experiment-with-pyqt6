import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton(self.hello_text())
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def hello_text(self):
        return requests.get(os.environ['API_URL'] + '/chatbot').text

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
