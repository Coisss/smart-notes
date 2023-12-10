import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QGridLayout

app = QApplication([])

window = QWidget()

layout_main = QHBoxLayout()

left_textEdit = QTextEdit()

list_notes_label = QLabel('Список заміток')
list_textEdit = QTextEdit()
list_add_btn = QPushButton('Створити замітку')
list_rem_btn = QPushButton('Видалити замітку')
list_sav_btn = QPushButton('Зберегти замітку')


layoutV_right = QVBoxLayout()
layoutV_left = QVBoxLayout()

layoutG_btn = QGridLayout()

layoutV_left.addWidget(left_textEdit)
layoutV_right.addWidget(list_notes_label)
layoutV_right.addWidget(list_textEdit)
layoutG_btn.addWidget(list_add_btn, 0, 0)
layoutG_btn.addWidget(list_rem_btn, 0, 1)
layoutG_btn.addWidget(list_sav_btn, 1, 0)


layout_main.addLayout(layoutV_left)
layout_main.addLayout(layoutV_right)
layoutV_right.addLayout(layoutG_btn)

window.setLayout(layout_main)

window.show()
app.exec_()