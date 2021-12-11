class Note:
    def __init__(self, name, note):

        if not isinstance(name, str):
            raise TypeError()
        elif name == "":
            raise ValueError()
        else:
            self.name = name

        if not isinstance(note, int) and not isinstance(note, float):
            raise TypeError()
        elif 2 <= note <= 6:
            self.note = note
        else:
            raise ValueError()

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note

