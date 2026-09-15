"""tests for text casing"""

from textutils.casing import capitalize_words


def test_capitalize():
    assert capitalize_words("hello world") == "Hello World"

def test_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"
