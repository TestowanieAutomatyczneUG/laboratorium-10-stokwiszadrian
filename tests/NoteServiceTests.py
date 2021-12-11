from src.NotesStorage import NotesStorage
from src.NotesService import NotesService
from src.Note import Note
from unittest.mock import *
from unittest import TestCase, main

class test_NotesService(TestCase):
    def setUp(self):
        self.storage = NotesStorage()
        self.storage.add = Mock(name='add')
        self.storage.clear = Mock(name='clear')
        self.storage.getAllNotesOf = Mock(name='getAllNotesOf')

    def test_NotesService_add(self):
        self.storage.add.return_value = True
        service = NotesService(self.storage)
        self.assertEqual(service.add(Note("test", 4)), True)

    def test_NotesService_averageOf(self):
        self.storage.getAllNotesOf.return_value = [4.5, 4.5, 3, 3, 5]
        service = NotesService(self.storage)
        self.assertEqual(service.averageOf("test"), 4)

    def test_NotesService_averageOf_empty(self):
        self.storage.getAllNotesOf.return_value = []
        service = NotesService(self.storage)
        self.assertFalse(service.averageOf("noname"))

    def test_NotesService_averageOf_float(self):
        self.storage.getAllNotesOf.return_value = [5, 4.5, 2]
        service = NotesService(self.storage)
        self.assertAlmostEqual(service.averageOf("test"), 3.83, 2)

    def test_NotesService_clear(self):
        self.storage.clear.return_value = []
        service = NotesService(self.storage)
        self.assertFalse(service.clear())

    def tearDown(self):
        self.storage = None


if __name__ == '__main__':
    main()