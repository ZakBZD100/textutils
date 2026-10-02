"""Tests for text casing functions."""

import pytest

from textutils.casing import capitalize_words


class TestCapitalizeWords:
    """Tests for the capitalize_words function."""

    def test_simple_string(self):
        """Capitalize each word in a simple string."""
        assert capitalize_words("hello world") == "Hello World"

    def test_empty_string(self):
        """Return an empty string for empty input."""
        assert capitalize_words("") == ""

    def test_already_capitalized(self):
        """Leave already-capitalized text unchanged."""
        assert capitalize_words("Hello World") == "Hello World"

    def test_multiple_words(self):
        """Capitalize all words in a longer string."""
        assert capitalize_words("open source development") == "Open Source Development"

    def test_none_input(self):
        """Return an empty string for None input."""
        assert capitalize_words(None) == ""

    def test_mixed_case(self):
        """Normalize mixed-case text."""
        assert capitalize_words("hELLO wORLD") == "Hello World"
