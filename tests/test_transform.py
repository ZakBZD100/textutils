"""tests pour transform"""

from textutils.transform import word_count, character_count, reverse, slugify, word_frequency


def test_word_count():
    assert word_count("Hello World") == 2

def test_word_count_empty():
    assert word_count("") == 0

def test_character_count():
    assert character_count("Hello") == 5

def test_character_count_none():
    assert character_count(None) == 0

def test_reverse():
    assert reverse("Hello") == "olleH"

def test_reverse_palindrome():
    assert reverse("racecar") == "racecar"

def test_slugify():
    assert slugify("Hello World") == "hello-world"

def test_slugify_special():
    assert slugify("Open Source!") == "open-source"

def test_word_frequency():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}

def test_word_frequency_empty():
    assert word_frequency("") == {}

def test_word_frequency_case():
    assert word_frequency("Hello hello HELLO") == {"hello": 3}

#todo: ajouter plus de tests plus tard
