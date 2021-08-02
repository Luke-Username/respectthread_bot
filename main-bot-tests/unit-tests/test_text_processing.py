# Modules
import sys                          # For terminal arguments and to import from different folders
import unittest                     # For unit testing
sys.path.insert(1, "../../main-bot")   # This path is to import modules to unit test.

# Functions to test
from text_processing import boundary
from text_processing import extract_match
from text_processing import strip_accents
from text_processing import valid_patterns_end
from text_processing import valid_patterns_start

class TestBoundary(unittest.TestCase):
    def test_non_special_word(self):
        self.assertEqual(boundary("a"), r"\ba\b")

    def test_start_round_bracket(self):
        self.assertEqual(boundary("\(a"), r"\(a\b")

    def test_round_brackets(self):
        self.assertEqual(boundary("\(a\)"), r"\(a\)")

    def test_question_mark(self):
        self.assertEqual(boundary("a?"), r"\ba?\b")

class TestExtractMatch(unittest.TestCase):
    def test_one_match(self):
        # Test that a match is found
        self.assertEqual(extract_match("a", "a"), "a")

    def test_two_matches(self):
        # Test that a match is found
        self.assertEqual(extract_match("a", "b a"), "a")

    def test_no_matches(self):
        # Test if the regex does not find any matche
        with self.assertRaises(TypeError):
            extract_match("a", "")

    def test_non_word_boundary(self):
        # Test that no match is found if the name is not surrounded by word boundaries
        with self.assertRaises(TypeError):
            extract_match("a", "ab")

class TestStripAccents(unittest.TestCase):
    def test_acute(self):
        # Test if the function can strip acute accents from strings
        self.assertEqual(strip_accents("é"), "e")
    
    def test_no_accents(self):
        # Test if the function does not change a string with no accents
        self.assertEqual(strip_accents("e"), "e")

class TestValidPatternsEnd(unittest.TestCase):
    def test_closing_round_bracket(self):
        self.assertFalse(valid_patterns_end("\\)"))

    def test_closing_square_bracket(self):
        self.assertFalse(valid_patterns_end("\\]"))
    
    def test_no_match_returns_true(self):
        self.assertTrue(valid_patterns_end(""))

class TestValidPatternsStart(unittest.TestCase):
    def test_opening_round_bracket(self):
        self.assertFalse(valid_patterns_start("\\("))
    
    def test_opening_square_bracket(self):
        self.assertFalse(valid_patterns_start("\\["))
    
    def test_no_match_returns_true(self):
        self.assertTrue(valid_patterns_start(""))
    