import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QInputDialog

PATH = os.path.dirname(__file__) + os.sep

def show_note():
    name = list_notes.selectedItems()[0].text()
    left_textEdit.setText(notes[name]["text"])
    list_tags.clear()
    list_tags.addItems(notes[name]["tags"])

def add_tag():
    selected_note = list_notes.selectedItems()
    if selected_note:
        name = selected_note[0].text()
        tag = search_tags.text()
        if tag and tag not in notes[name]["tags"]:
            notes[name]["tags"].append(tag)
            list_tags.clear()
            list_tags.addItems(notes[name]["tags"])

def remove_tag():
    selected_note = list_notes.selectedItems()
    if selected_note:
        name = selected_note[0].text()
        selected_tags = list_tags.selectedItems()
        if selected_tags:
            tag = selected_tags[0].text()
            notes[name]["tags"].remove(tag)
            list_tags.clear()
            list_tags.addItems(notes[name]["tags"])

def search_by_tag():
    tag = search_tags.text()
    if tag:
        matching_notes = [note for note, data in notes.items() if tag in data["tags"]]
        list_notes.clear()
        list_notes.addItems(matching_notes)

def create_note():
    new_note_name, ok = QInputDialog.getText(window, 'Создать заметку', 'Введите название новой заметки:')
    if ok and new_note_name:
        notes[new_note_name] = {"text": "", "tags": []}
        list_notes.addItem(new_note_name)
        save_notes()

def remove_note():
    selected_note = list_notes.selectedItems()
    if selected_note:
        name = selected_note[0].text()
        del notes[name]
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        save_notes()

def save_notes():
    current_note = list_notes.currentItem()
    if current_note:
        name = current_note.text()
        notes[name]["text"] = left_textEdit.toPlainText()

    with open(PATH + "test.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)

app = QApplication([])

window = QWidget()

# проверка наличие файла test.json
if os.path.isfile(PATH + "test.json"):
    with open(PATH + "test.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
else:
    notes = {}

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

# правый. заметки
layoutV_right.addWidget(list_notes_label)
layoutV_right.addWidget(list_notes)

# добавление кнопок заметок в один вертикальный лэйаут
layoutH1_btn.addWidget(list_add_btn)
layoutH1_btn.addWidget(list_rem_btn)
layoutH2_btn.addWidget(list_sav_btn)

# добавление лэйаута кнопок заметок в правый вертикальный лэйаут
layoutV_right.addLayout(layoutH1_btn)
layoutV_right.addLayout(layoutH2_btn)

# правый. теги
layoutV_right.addWidget(label_tags)
layoutV_right.addWidget(list_tags)
layoutV_right.addWidget(search_tags)

# добавление кнопок тегов в один вертикальный лэйаут
layout2H1_btn.addWidget(tags_add_btn)
layout2H1_btn.addWidget(tags_rem_btn)
layout2H2_btn.addWidget(tags_sav_btn)

# добавление лэйаута кнопок тегов в правый вертикальный лэйаут
layoutV_right.addLayout(layout2H1_btn)
layoutV_right.addLayout(layout2H2_btn)

# добавление лэйаутов левый и правый в один целый
layout_main.addLayout(layoutV_left)
layout_main.addLayout(layoutV_right)

window.setLayout(layout_main)

list_notes.addItems(notes)

list_notes.itemClicked.connect(show_note)
tags_add_btn.clicked.connect(add_tag)
tags_rem_btn.clicked.connect(remove_tag)
tags_sav_btn.clicked.connect(search_by_tag)
list_add_btn.clicked.connect(create_note)
list_rem_btn.clicked.connect(remove_note)
list_sav_btn.clicked.connect(save_notes)

# Добавляем обработчик изменения текста заметки
left_textEdit.textChanged.connect(save_notes)

window.show()
app.exec_()
