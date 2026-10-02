"""Tests for text casing functions."""

import pytest

from textutils.casing import capitalize_words, snake_case


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


class TestSnakeCase:
    """Tests for the snake_case function."""

    def test_simple_string(self):
        """Convert a space-separated string to snake_case."""
        assert snake_case("Hello World") == "hello_world"

    def test_hyphenated_string(self):
        """Convert a hyphenated string to snake_case."""
        assert snake_case("hello-world") == "hello_world"

    def test_camel_case_string(self):
        """Convert camelCase to snake_case."""
        assert snake_case("HelloWorld") == "hello_world"

    def test_already_snake_case(self):
        """Leave an already snake_case string unchanged."""
        assert snake_case("hello_world") == "hello_world"

    def test_empty_string(self):
        """Return an empty string for empty input."""
        assert snake_case("") == ""

    def test_none_input(self):
        """Return an empty string for None input."""
        assert snake_case(None) == ""

    def test_single_word(self):
        """Convert a single lowercase word."""
        assert snake_case("hello") == "hello"

    def test_multiple_words(self):
        """Convert a multi-word string."""
        assert snake_case("Open Source Development") == "open_source_development"
