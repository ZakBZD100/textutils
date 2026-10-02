"""Text transformation functions for counting and manipulating strings."""


def word_count(text: str) -> int:
    """Count the number of words in a text.

    Words are separated by whitespace characters.

    Args:
        text: The input text to count words in.

    Returns:
        The number of words in the text. Returns 0 if text is empty or None.

    Examples:
        >>> word_count("Hello World")
        2
        >>> word_count("")
        0
    """
    if not text or not text.strip():
        return 0
    return len(text.split())


def character_count(text: str) -> int:
    """Count the number of characters in a text.

    Spaces and punctuation are included in the count.

    Args:
        text: The input text to count characters in.

    Returns:
        The number of characters in the text. Returns 0 if text is None.

    Examples:
        >>> character_count("Hello")
        5
        >>> character_count("")
        0
    """
    if text is None:
        return 0
    return len(text)


def reverse(text: str) -> str:
    """Reverse a given text string.

    Args:
        text: The input text to reverse.

    Returns:
        The reversed text. Returns an empty string if text is None.

    Examples:
        >>> reverse("Hello")
        'olleH'
        >>> reverse("racecar")
        'racecar'
    """
    if text is None:
        return ""
    return text[::-1]


def slugify(text: str) -> str:
    """Generate a URL-friendly slug from a text.

    Converts text to lowercase, replaces spaces and special characters
    with hyphens, and removes consecutive hyphens.

    Args:
        text: The input text to slugify.

    Returns:
        A URL-safe slug string. Returns an empty string if text is None.

    Examples:
        >>> slugify("Hello World")
        'hello-world'
        >>> slugify("Open Source Development!")
        'open-source-development'
        >>> slugify("  Multiple   Spaces  ")
        'multiple-spaces'
    """
    if text is None:
        return ""
    import re

    # Lowercase, replace non-alphanumeric with hyphens, collapse hyphens
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")
