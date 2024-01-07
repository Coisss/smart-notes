import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QInputDialog

class Design():
    def __init__(self,PATH):
        self.app = QApplication([])

        self.window = QWidget()

        # проверка наличие файла test.json
        if os.path.isfile(PATH + "test.json"):
            with open(PATH + "test.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        else:
            self.notes = {}

        self.layout_main = QHBoxLayout()

        self.window.setWindowTitle('Заметки')

        # список заметок
        self.list_notes_label = QLabel('Список заметок')
        self.left_textEdit = QTextEdit()
        self.list_notes = QListWidget()
        self.list_add_btn = QPushButton('Создать заметку')
        self.list_rem_btn = QPushButton('Удалить замтеку')
        self.list_sav_btn = QPushButton('Сохранить заметку')

        # список тегов
        self.label_tags = QLabel('Список тегов')
        self.list_tags = QListWidget()
        self.search_tags = QLineEdit()
        self.tags_add_btn = QPushButton('Добавить к заметке')
        self.tags_rem_btn = QPushButton('Открепить от заметки')
        self.tags_sav_btn = QPushButton('Искать заметки по тег')

        self.layoutV_right = QVBoxLayout()
        self.layoutV_left = QVBoxLayout()

        # кнопки 1
        self.layoutV_btn = QVBoxLayout()
        self.layoutH1_btn = QHBoxLayout()
        self.layoutH2_btn = QHBoxLayout()

        # кнопки 2
        self.layout2V_btn = QVBoxLayout()
        self.layout2H1_btn = QHBoxLayout()
        self.layout2H2_btn = QHBoxLayout()

        # левый
        self.layoutV_left.addWidget(self.left_textEdit)

        # правый. заметки
        self.layoutV_right.addWidget(self.list_notes_label)
        self.layoutV_right.addWidget(self.list_notes)

        # добавление кнопок заметок в один вертикальный лэйаут
        self.layoutH1_btn.addWidget(self.list_add_btn)
        self.layoutH1_btn.addWidget(self.list_rem_btn)
        self.layoutH2_btn.addWidget(self.list_sav_btn)

        # добавление лэйаута кнопок заметок в правый вертикальный лэйаут
        self.layoutV_right.addLayout(self.layoutH1_btn)
        self.layoutV_right.addLayout(self.layoutH2_btn)

        # правый. теги
        self.layoutV_right.addWidget(self.label_tags)
        self.layoutV_right.addWidget(self.list_tags)
        self.layoutV_right.addWidget(self.search_tags)

        # добавление кнопок тегов в один вертикальный лэйаут
        self.layout2H1_btn.addWidget(self.tags_add_btn)
        self.layout2H1_btn.addWidget(self.tags_rem_btn)
        self.layout2H2_btn.addWidget(self.tags_sav_btn)

        # добавление лэйаута кнопок тегов в правый вертикальный лэйаут
        self.layoutV_right.addLayout(self.layout2H1_btn)
        self.layoutV_right.addLayout(self.layout2H2_btn)

        # добавление лэйаутов левый и правый в один целый
        self.layout_main.addLayout(self.layoutV_left)
        self.layout_main.addLayout(self.layoutV_right)

        self.window.setLayout(self.layout_main)

        self.list_notes.addItems(self.notes)

        # Стиль для списков и элементов списка
        list_style = """
            QListWidget, QLineEdit, QTextEdit {
                background-color: #ffffff;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
            }
            QListWidget:item {
                background-color: #f0f0f0;
                padding: 5px;
                border-radius: 3px;
                margin-bottom: 5px;
            }
            QListWidget:item:selected {
                background-color: #4CAF50;
                color: white;
            }
        """
        
        # Стиль для кнопок
        button_style = """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
            }
        """

        # Стиль для фона
        background_style = """
            QWidget { 
                background-color: #f0f0f0;
            }
        """

        # Применение стилей
        self.list_notes.setStyleSheet(list_style)
        self.list_tags.setStyleSheet(list_style)
        self.search_tags.setStyleSheet(list_style)
        self.left_textEdit.setStyleSheet(list_style)

        self.list_add_btn.setStyleSheet(button_style)
        self.list_rem_btn.setStyleSheet(button_style)
        self.list_sav_btn.setStyleSheet(button_style)
        self.tags_add_btn.setStyleSheet(button_style)
        self.tags_rem_btn.setStyleSheet(button_style)
        self.tags_sav_btn.setStyleSheet(button_style)

        self.window.setStyleSheet(background_style)

    def init(self):
        self.list_notes.itemClicked.connect(self.show_note)
        self.tags_add_btn.clicked.connect(self.add_tag)
        self.tags_rem_btn.clicked.connect(self.remove_tag)
        self.tags_sav_btn.clicked.connect(self.search_by_tag)
        self.list_add_btn.clicked.connect(self.create_note)
        self.list_rem_btn.clicked.connect(self.remove_note)
        self.list_sav_btn.clicked.connect(self.save_notes)

        # Добавляем обработчик изменения текста заметки
        self.left_textEdit.textChanged.connect(self.save_notes)

        self.window.show()
        self.app.exec_()    