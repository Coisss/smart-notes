import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QInputDialog
from logic import Program
from design import Design

PATH = os.path.dirname(__file__) + os.sep

design = Design(PATH)
program = Program(PATH,design)


