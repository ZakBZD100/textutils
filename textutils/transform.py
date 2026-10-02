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
