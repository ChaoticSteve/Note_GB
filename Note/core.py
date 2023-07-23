from datetime import datetime
import json
class NoteService():
    def __init__(self):
        self.notes = {}
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
    def delNote(self):
        pass
    def addNote(self):
        note_title = input('Заголовок заметки: ')
        note_txt = input('Тело заметки: ')
        note_date = str(datetime.now())[:10]
        self.id += 1
        if note_date not in self.notes:
            self.notes[note_date] = {note_title :{'id' : self.id, 'text' : note_txt}}
        else:
            self.notes[note_date][note_title] = {'id' : self.id, 'text' : note_txt}
        self.saveNotes()
    def editNote(self):
        pass
    def countID(self):
        count = 0
        for key in self.notes:
            count += len(self.notes[key])
        return count


#print(str(datetime.now())[:10])
if __name__ == '__main__':
    ns = NoteService()
    ns.addNote()
