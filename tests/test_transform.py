"""Tests for text transformation functions."""

import pytest

from textutils.transform import character_count, reverse, slugify, word_count


class TestWordCount:
    """Tests for the word_count function."""

    def test_simple_sentence(self):
        """Count words in a simple sentence."""
        assert word_count("Hello World") == 2

    def test_empty_string(self):
        """Return 0 for an empty string."""
        assert word_count("") == 0

    def test_single_word(self):
        """Count a single word."""
        assert word_count("Hello") == 1

    def test_multiple_spaces(self):
        """Collapse multiple spaces between words."""
        assert word_count("Hello   World") == 2

    def test_leading_trailing_spaces(self):
        """Ignore leading and trailing whitespace."""
        assert word_count("  Hello World  ") == 2

    def test_none_input(self):
        """Return 0 for None input."""
        assert word_count(None) == 0

    def test_whitespace_only(self):
        """Return 0 for whitespace-only input."""
        assert word_count("   ") == 0


class TestCharacterCount:
    """Tests for the character_count function."""

    def test_simple_string(self):
        """Count characters in a simple string."""
        assert character_count("Hello") == 5

    def test_empty_string(self):
        """Return 0 for an empty string."""
        assert character_count("") == 0

    def test_with_spaces(self):
        """Include spaces in the count."""
        assert character_count("Hello World") == 11

    def test_none_input(self):
        """Return 0 for None input."""
        assert character_count(None) == 0

    def test_single_character(self):
        """Count a single character."""
        assert character_count("a") == 1


class TestReverse:
    """Tests for the reverse function."""

    def test_simple_string(self):
        """Reverse a simple string."""
        assert reverse("Hello") == "olleH"

    def test_empty_string(self):
        """Return an empty string for empty input."""
        assert reverse("") == ""

    def test_palindrome(self):
        """Return the same string for a palindrome."""
        assert reverse("racecar") == "racecar"

    def test_none_input(self):
        """Return an empty string for None input."""
        assert reverse(None) == ""

    def test_with_spaces(self):
        """Preserve spaces when reversing."""
        assert reverse("ab cd") == "dc ba"


class TestSlugify:
    """Tests for the slugify function."""

    def test_simple_string(self):
        """Convert a simple string to a slug."""
        assert slugify("Hello World") == "hello-world"

    def test_with_punctuation(self):
        """Remove punctuation from the slug."""
        assert slugify("Open Source Development!") == "open-source-development"

    def test_multiple_spaces(self):
        """Collapse multiple spaces into single hyphens."""
        assert slugify("  Multiple   Spaces  ") == "multiple-spaces"

    def test_empty_string(self):
        """Return an empty string for empty input."""
        assert slugify("") == ""

    def test_none_input(self):
        """Return an empty string for None input."""
        assert slugify(None) == ""

    def test_already_slug(self):
        """Leave an already valid slug unchanged."""
        assert slugify("hello-world") == "hello-world"

    def test_special_characters(self):
        """Replace special characters with hyphens."""
        assert slugify("user@example.com") == "user-example-com"

    def test_numbers(self):
        """Preserve numbers in the slug."""
        assert slugify("Python 3.11 Release") == "python-3-11-release"
