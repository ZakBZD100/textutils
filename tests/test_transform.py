"""tests for text transformations"""

from textutils.transform import word_count, character_count, reverse


def test_word_count():
    assert word_count("Hello World") == 2

def test_word_count_empty():
    assert word_count("") == 0

def test_character_count():
    assert character_count("Hello") == 5

def test_reverse():
    assert reverse("Hello") == "olleH"

#need to add tests for None input later
