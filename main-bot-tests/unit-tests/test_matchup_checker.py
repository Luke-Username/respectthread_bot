# Modules
import sys                          # For terminal arguments and to import from different folders
import unittest                     # For unit testing
sys.path.insert(1, "../../main-bot")   # This path is to import modules to unit test.

# Functions to test
from character import Character
from matchup_checker import add_to_reply
from matchup_checker import check_version_array
from matchup_checker import is_rt_in_post
from matchup_checker import post_contains
from unittest.mock import patch

class TestAddToReply(unittest.TestCase):
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Set up fake database connection
        self.mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        self.mock_cur = self.mock_con.cursor.return_value  # result of con.cursor()

        # Start with an empty character list
        self.character_list = []

    def test_empty_respectthread_ids_does_not_add_to_character_list(self):
        add_to_reply("TestName", "TestDefaultName", "TestVerseName", [], self.character_list, "Test post", self.mock_cur)
        self.assertEqual(len(self.character_list), 0)

    @patch("matchup_checker.is_rt_in_post")
    def test_id_not_in_respectthread_list_append_character_list(self, mock_is_rt_in_post):
        # Set the function call's output value, so the test does not have to depend on it.
        mock_is_rt_in_post.return_value = False
        add_to_reply("TestName", "TestDefaultName", "TestVerseName", [0], self.character_list, "Test post", self.mock_cur)
        new_char = Character("TestName", "TestDefaultName", "TestVerseName", [0])
        self.assertEqual(len(self.character_list), len([new_char]))

class TestCheckVersionArray(unittest.TestCase):
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Set up fake database connection
        self.mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        self.mock_cur = self.mock_con.cursor.return_value  # result of con.cursor()

    def test_empty_versions(self):
        self.assertTrue(check_version_array([], "", self.mock_cur))

    def test_post_does_not_contain_version(self):
        self.assertFalse(check_version_array(["a"], "b", self.mock_cur))

    def test_post_does_contain_version(self):
        # Mock the return value of fetching one row.
        # This will also partially test post_contains() in the case there are no name conflicts. 
        self.mock_cur.fetchone.return_value = [(0)]
        self.assertTrue(check_version_array(["a"], "a", self.mock_cur))

    def test_post_does_contain_version_list_size_two(self):
        self.assertFalse(check_version_array(["a", "b"], "b", self.mock_cur))

class TestIsRtInPost(unittest.TestCase): 
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Set up fake database connection
        self.mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        self.mock_cur = self.mock_con.cursor.return_value  # result of con.cursor()

    def test_match_shortlink_returns_true(self):
        self.mock_cur.fetchone.return_value = [("https://redd.it/test1a")]
        self.assertTrue(is_rt_in_post(0, "test1a", self.mock_cur))

    def test_match_longlink_returns_true(self):
        self.mock_cur.fetchone.return_value = [("https://www.reddit.com/r/respectthreads/comments/bccj18/kevin_wendell_crumb_the_horde_unbreakable_trilogy/ekpghf8/")]
        self.assertTrue(is_rt_in_post(0, "bccj18", self.mock_cur))

    def test_no_match_returns_false(self):
        self.mock_cur.fetchone.return_value = [("https://redd.it/test1a")]
        self.assertFalse(is_rt_in_post(0, "", self.mock_cur))

class TestPostContains(unittest.TestCase):
    @patch("psycopg2.connect")
    def setUp(self, mock_connect):
        # Set up fake database connection
        self.mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        self.mock_cur = self.mock_con.cursor.return_value  # result of con.cursor()
    
    def test_no_pattern_match_returns_false(self):
        self.assertFalse(post_contains("a", "", self.mock_cur))
        self.assertFalse(post_contains("a", "b", self.mock_cur))

    def test_no_name_conflicts_returns_true(self):
        # Mock the return value of fetching one row.
        self.mock_cur.fetchone.return_value = [(0)]
        self.assertTrue(post_contains("a", "a", self.mock_cur))

    def test_yes_name_conflicts_returns_true(self):
        # Mock the return value of fetching one row, and of fetching all rows.
        self.mock_cur.fetchone.return_value = [(1)]
        self.mock_cur.fetchall.return_value = [("a c", -2)]
        self.assertTrue(post_contains("c", "c a c", self.mock_cur))
    
    # If a match is found, but the only match has a name conflict, it should return false. 
    def test_yes_name_conflicts_returns_false(self):
        # Mock the return value of fetching one row.
        self.mock_cur.fetchone.return_value = [(1)]
        self.mock_cur.fetchall.return_value = [("a c", -2)]
        self.assertFalse(post_contains("c", "a c", self.mock_cur))