"""textutils - une petite librairie de manipulation de texte"""

from textutils.casing import capitalize_words, snake_case, camel_case
from textutils.transform import (
    word_count,
    character_count,
    reverse,
    slugify,
    word_frequency,
)

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "slugify",
    "word_frequency",
    "capitalize_words",
    "snake_case",
    "camel_case",
]

__version__ = "0.3.0"
