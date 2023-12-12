import json, os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QGridLayout, QListWidget

PATH = os.path.dirname(__file__) + os.sep

def show_note():
    name = list_notes.selectedItems()[0].text()
    left_textEdit.setText(notes[name]["text"])
    # list_tags.clear()
    # list_tags.setText(notes[name]["tags"])

app = QApplication([])

window = QWidget()

notes = {
    "Cool": {
        "text": "I am cool guy",
        "tags": ["Super_guy", "Cooool"]
    },
    "Oleg": {
        "text": "Пайтон",
        "tags": ["Lorem Ipsum", "Dolor sit amet"]
    }
}

# Запись словаря в файл JSON

with open("test.json", "w") as file:
    json.dump(notes, file)

layout_main = QHBoxLayout()

# список заметок
list_notes_label = QLabel('Список заміток')
left_textEdit = QTextEdit()
list_notes = QListWidget()
list_add_btn = QPushButton('Створити замітку')
list_rem_btn = QPushButton('Видалити замітку')
list_sav_btn = QPushButton('Зберегти замітку')


# список тегов
label_tags = QLabel('Список тегов')
list_tags = QListWidget()
search_tags = QLineEdit()
tags_add_btn = QPushButton('Добавить к заметке')
tags_rem_btn = QPushButton('Открепить от заметки')
tags_sav_btn = QPushButton('Искать заметки по тег')

layoutV_right = QVBoxLayout()
layoutV_left = QVBoxLayout()

# кнопки 1
layoutV_btn = QVBoxLayout()
layoutH1_btn = QHBoxLayout()
layoutH2_btn = QHBoxLayout()

# кнопки 2
layout2V_btn = QVBoxLayout()
layout2H1_btn = QHBoxLayout()
layout2H2_btn = QHBoxLayout()

# левый
layoutV_left.addWidget(left_textEdit)

# правый
layoutV_right.addWidget(list_notes_label)
layoutV_right.addWidget(list_notes)

layoutV_right.addWidget(label_tags)
layoutV_right.addWidget(list_tags)
layoutV_right.addWidget(search_tags)

# добавление кнопок в горизонтальные лэйауты
layout2H1_btn.addWidget(list_add_btn)
layout2H1_btn.addWidget(list_rem_btn)
layout2H2_btn.addWidget(list_sav_btn)

# добавление кнопок2 в горизонтальные лэйауты
layoutH1_btn.addWidget(tags_add_btn)
layoutH1_btn.addWidget(tags_rem_btn)
layoutH2_btn.addWidget(tags_sav_btn)

# добавление лэйаутов левый правый в один целый
layout_main.addLayout(layoutV_left)
layout_main.addLayout(layoutV_right)

# добавление горизонт лэйаутов кнопок в один целый вертикальный 
layoutV_btn.addLayout(layoutH1_btn)
layoutV_btn.addLayout(layoutH2_btn)

# добавление кнопок 1 в верт лэйаут
layoutV_right.addLayout(layoutV_btn)

# добавление горизонт лэйаутов кнопок 2 в один целый вертикальный 
layoutV_btn.addLayout(layout2H1_btn)
layoutV_btn.addLayout(layout2H2_btn)

# добавление кнопок 2 в верт лэйаут
layoutV_right.addLayout(layout2V_btn)

window.setLayout(layout_main)

with open(PATH + "test.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
list_notes.addItems(notes)

list_notes.itemClicked.connect(show_note)

print(notes)

window.show()
app.exec_()