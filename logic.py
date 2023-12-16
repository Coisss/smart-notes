import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QInputDialog


class Program():
    def __init__(self,PATH,DESIGN):
        self.design = DESIGN
        self.PATH = PATH
        DESIGN.show_note = self.show_note
        DESIGN.add_tag = self.add_tag
        DESIGN.remove_tag = self.remove_tag
        DESIGN.search_by_tag = self.search_by_tag
        DESIGN.create_note = self.create_note
        DESIGN.remove_note = self.remove_note
        DESIGN.save_notes = self.save_notes

 
        DESIGN.init()
        
    def show_note(self):
        name = self.design.list_notes.selectedItems()[0].text()
        self.design.left_textEdit.setText(self.design.notes[name]["text"])
        self.design.list_tags.clear()
        self.design.list_tags.addItems(self.design.notes[name]["tags"])

    def add_tag(self):
        selected_note = self.design.list_notes.selectedItems()
        if selected_note:
            name = selected_note[0].text()
            tag = self.design.search_tags.text()
            if tag and tag not in self.design.notes[name]["tags"]:
                self.design.notes[name]["tags"].append(tag)
                self.design.list_tags.clear()
                self.design.list_tags.addItems(self.design.notes[name]["tags"])

    def remove_tag(self):
        selected_note = self.design.list_notes.selectedItems()
        if selected_note:
            name = selected_note[0].text()
            selected_tags = self.design.list_tags.selectedItems()
            if selected_tags:
                tag = selected_tags[0].text()
                self.design.notes[name]["tags"].remove(tag)
                self.design.list_tags.clear()
                self.design.list_tags.addItems(self.design.notes[name]["tags"])

    def search_by_tag(self):
        tag = self.design.search_tags.text()
        if tag:
            matching_notes = [note for note, data in self.design.notes.items() if tag in data["tags"]]
            self.design.list_notes.clear()
            self.design.list_notes.addItems(matching_notes)
        else:
            matching_notes = [note for note, data in self.design.notes.items()]
            self.design.list_notes.clear()
            self.design.list_notes.addItems(matching_notes)
    def create_note(self):
        new_note_name, ok = QInputDialog.getText(self.design.window, 'Создать заметку', 'Введите название новой заметки:')
        if ok and new_note_name:
            self.design.notes[new_note_name] = {"text": "", "tags": []}
            self.design.list_notes.addItem(new_note_name)
            self.design.save_notes()

    def remove_note(self):
        selected_note = self.design.list_notes.selectedItems()
        if selected_note:
            name = selected_note[0].text()
            del self.design.notes[name]
            self.design.list_notes.clear()
            self.design.list_tags.clear()
            self.design.list_notes.addItems(self.design.notes)
            self.design.save_notes()

    def save_notes(self):
        current_note = self.design.list_notes.currentItem()
        if current_note:
            name = current_note.text()
            self.design.notes[name]["text"] = self.design.left_textEdit.toPlainText()

        with open(self.PATH + "test.json", "w", encoding="utf-8") as file:
            json.dump(self.design.notes, file)