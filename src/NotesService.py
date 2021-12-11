from src.NotesStorage import NotesStorage

class NotesService():
    def __init__(self, storage: NotesStorage):
        self.storage = storage

    def add(self, note):
        return self.storage.add(note)

    def averageOf(self, name):
        notes = self.storage.getAllNotesOf(name)
        if len(notes) == 0:
            return 0
        else:
            return sum(notes)/len(notes)

    def clear(self):
        return self.storage.clear()
