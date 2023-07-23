from datetime import datetime
import json


class NoteService():
    def __init__(self):
        self.notes = {'freeID': []}
        self.getNotes()
        self.id = self.countID()

    def getNotes(self):
        try:
            with open('notes_data,json', 'r', encoding='utf-8') as f:
                self.notes = json.load(f)
        except IOError as e:
            self.saveNotes()

    def saveNotes(self):
        with open('notes_data,json', 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, sort_keys=True, ensure_ascii=False)

    def getAllDates(self):
        dates = ', '.join([key for key in self.notes.keys()]).replace(', freeID', '')
        print('Доступные даты:', dates)

    def delNote(self, key):
        key = key
        title = self.getNote(key)
        if title:
            self.notes['freeID'].append(self.notes[key][title]['id'] - 1)
            self.notes['freeID'].sort()
            del self.notes[key][title]
            print('Заметка удалена')
            self.saveNotes()

    def addNote(self):
        note_title = input('Заголовок заметки: ')
        note_txt = input('Тело заметки: ')
        note_date = str(datetime.now())[:10]
        self.id += 1
        if note_date not in self.notes:
            self.notes[note_date] = {note_title: {'id': self.id, 'text': note_txt}}
        else:
            self.notes[note_date][note_title] = {'id': self.id, 'text': note_txt}
        print('Заметка создана')
        self.saveNotes()

    def editNote(self, key):
        key = key
        date = str(datetime.now())[:10]
        title = self.getNote(key)
        if title:
            text = input('Введите текст:\n')
            if date == key:
                self.notes[key][title]['text'] += ' ' + text
            else:
                self.notes[date][title] = self.notes[key][title]
                self.notes[date][title]['text'] += ' ' + text
                del self.notes[key][title]
            print('Заметка изменена')
            self.saveNotes()

    def getNote(self, key):
        key = key
        try:
            print('Доступные заметки: ', *self.notes[key].keys())
            title = input('Введите название заметки: ')
            print('Текущий текст заметки:\n', self.notes[key][title]['text'])
            return title
        except KeyError as e:
            print('Данной заметки нет')
            return False

    def countID(self):
        if len(self.notes['freeID']):
            return self.notes['freeID'].pop(0)
        count = 0
        for key in self.notes:
            count += len(self.notes[key])
        return count


# print(str(datetime.now())[:10])
if __name__ == '__main__':
    ns = NoteService()
    # ns.addNote()
    # ns.editNote()
    # ns.delNote()
    ns.getAllDates()
