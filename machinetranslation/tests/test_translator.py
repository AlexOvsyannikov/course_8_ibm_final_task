import unittest
from translator import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null_input(self):
        self.assertEqual(french_to_english(''), '')

    def test_for_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Good morning')


class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_input(self):
        self.assertEqual(english_to_french(''), '')

    def test_for_bonjour(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


unittest.main()
