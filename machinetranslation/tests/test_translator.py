"""Tests for translate module"""
import unittest
from ..translator import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase):
    """Class tot test french_to_english function"""
    def test_for_null_input(self):
        """Checking if null input returns an empty string"""
        self.assertEqual(french_to_english(''), '')

    def test_for_bonjour(self):
        """Checkig if translation works properly"""
        self.assertEqual(french_to_english('Bonjour'), 'Good morning')


class TestEnglishToFrench(unittest.TestCase):
    """Class tot test english_to_french function"""
    def test_for_null_input(self):
        """Checking if null input returns an empty string"""
        self.assertEqual(english_to_french(''), '')

    def test_for_bonjour(self):
        """Checkig if translation works properly"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
