"""textutils - A lightweight Python library for common text-processing operations."""

from textutils.casing import camel_case, capitalize_words, snake_case
from textutils.transform import character_count, reverse, slugify, word_count

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "capitalize_words",
    "snake_case",
    "camel_case",
    "slugify",
]
__version__ = "0.1.0"
