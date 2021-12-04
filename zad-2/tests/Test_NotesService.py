import unittest
from modules.NotesStorage import NotesStorage
from modules.NotesService import NotesService
from modules.Note import Note
from unittest.mock import MagicMock, Mock, patch


class Test_NotesService(unittest.TestCase):
	@patch("modules.NotesStorage.add")
	def test_add_returning_added_note(self, mock_NotesStorage_add: MagicMock):
		notesService = NotesService()
		note = Note("test", 3)
		mock_NotesStorage_add.return_value = note
		addedNote = notesService.add(note)
		self.assertEqual(addedNote, note)
	@patch("modules.NotesStorage.getAllNotesOf")
	def test_averageOf(self, mock_NotesStorage_getAllNotesOf: MagicMock):
		notesService = NotesService()
		mock_NotesStorage_getAllNotesOf.return_value = set([Note("test", 3), Note("test", 5)])
		self.assertEqual(notesService.averageOf("test"), 4)
	@patch("modules.NotesStorage.getAllNotesOf")
	def test_averageOf_with_no_notes(self, mock_NotesStorage_getAllNotesOf: MagicMock):
		notesService = NotesService()
		mock_NotesStorage_getAllNotesOf.return_value = set()
		self.assertIsNone(notesService.averageOf("test"))
	@patch("modules.NotesStorage.clear")
	def test_clear(self, mock_NotesStorage_clear: MagicMock):
		mock_NotesStorage_clear.return_value = None
		notesService = NotesService()
		self.assertIsNone(notesService.clear())