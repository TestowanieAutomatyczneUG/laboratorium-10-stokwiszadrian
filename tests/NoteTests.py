import unittest
from src.Note import Note


class NoteTests(unittest.TestCase):
    def test_note_getname(self):
        self.assertEqual(Note("testname", 3).get_name(), "testname")

    def test_note_getname_none(self):
        self.assertRaises(TypeError, Note, None, 4)

    def test_note_name_empty(self):
        self.assertRaises(ValueError, Note, "", 4)

    def test_note_name_list(self):
        self.assertRaises(TypeError, Note, ["test"], 5)

    def test_note_getnote_int(self):
        self.assertEqual(Note("testname", 3).get_note(), 3)

    def test_note_getnote_float(self):
        self.assertEqual(Note("testname", 4.5).get_note(), 4.5)

    def test_note_toobig(self):
        self.assertRaises(ValueError, Note, "test", 7)

    def test_note_toolow(self):
        self.assertRaises(ValueError, Note, "test", 0.4)

    def test_note_string_note(self):
        self.assertRaises(TypeError, Note, "test", "4")

    def test_note_list_note(self):
        self.assertRaises(TypeError, Note, "test", [4])