# Modules
import sys                          # For terminal arguments and to import from different folders
import unittest                     # For unit testing
sys.path.insert(1, "../../main-bot")   # This path is to import modules to unit test.

# Functions to test
from character import Character
from replier import generate_comment
from unittest.mock import patch

class TestGenerateComment(unittest.TestCase):
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Set up fake database connection
        self.mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        self.mock_cur = self.mock_con.cursor.return_value  # result of con.cursor()

        # Set up fake characters
        self.character_1 = Character("TestName1", "TestDefaultName1", "TestVerse1", [0])
        self.character_2 = Character("TestName2", "TestDefaultName2", "TestVerse2", [1])

    # Test that adding one character to the reply looks okay
    def test_one_character(self):
        character_list = [self.character_1]
        self.mock_cur.fetchall.return_value = [(0, "RT Title", "https://redd.it/Testin")]
        expected_reply_text = "**TestName1 (TestVerse1)**\n\n"
        expected_reply_text += "- [RT Title](https://redd.it/Testin)\n\n"
        self.assertEqual(generate_comment(self.mock_cur, character_list, False), expected_reply_text)
    
    # Test that adding two characters to the reply looks okay
    def test_two_characters(self):
        character_list = [self.character_1, self.character_2]
        self.mock_cur.fetchall.return_value = [(0, "RT Title", "https://redd.it/Testin"), (1, "RT Title 2", "https://redd.it/Test2n")]
        expected_reply_text = "**TestName1 (TestVerse1)**\n\n"
        expected_reply_text += "- [RT Title](https://redd.it/Testin)\n\n"
        expected_reply_text += "- [RT Title 2](https://redd.it/Test2n)\n\n"
        expected_reply_text += "**TestName2 (TestVerse2)**\n\n"
        expected_reply_text += "- [RT Title](https://redd.it/Testin)\n\n"
        expected_reply_text += "- [RT Title 2](https://redd.it/Test2n)\n\n"
        self.assertEqual(generate_comment(self.mock_cur, character_list, False), expected_reply_text)