import unittest
from modules.Note import Note
from parameterized import parameterized

class Test_Note(unittest.TestCase):
	def test_ok(self):
		Note("rafał", 5) # will raise an exception if something goes wrong
		self.assertTrue(True)
	def test_empty_name(self):
		self.assertRaises(ValueError, Note, "", 5)
	def test_too_small_grade(self):
		self.assertRaises(ValueError, Note, "rafał", 1.9)
	def test_too_big_grade(self):
		self.assertRaises(ValueError, Note, "rafał", 6.1)
	@parameterized.expand([
		("rafał", 2),
		("rafał", 3),
		("rafał", 4),
		("rafał", 5),
		("rafał", 6)
	])
	def test_valid_grade(self, name, grade):
		Note(name, grade)
		self.assertTrue(True)
	def test_no_name(self):
		self.assertRaises(ValueError, Note, None, 5)
	def test_wrong_name_type(self):
		self.assertRaises(TypeError, Note, 1, 5)
	def test_no_grade(self):
		self.assertRaises(TypeError, Note, "rafał", None)
	def test_wrong_grade_type(self):
		self.assertRaises(TypeError, Note, "rafał", "5")
	def test_name_getter(self):
		note = Note("rafał", 5)
		self.assertEqual(note.name, "rafał")
	def test_note_getter(self):
		note = Note("rafał", 5)
		self.assertEqual(note.note, 5)
	def test_str(self):
		note = Note("rafał", 5)
		self.assertEqual(str(note), f"""Note(name = "rafał", note = 5)""")
	def test_repr(self):
		note = Note("rafał", 5)
		self.assertEqual(repr(note), f"""Note(name = "rafał", note = 5)""")
	def test_eq(self):
		note1 = Note("rafał", 5)
		note2 = Note("rafał", 5)
		self.assertEqual(note1, note2)
	def test_neq(self):
		note1 = Note("rafał", 5)
		note2 = Note("rafał", 6)
		self.assertNotEqual(note1, note2)



