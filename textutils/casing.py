"""Text casing functions for converting between different text formats."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a text.

    Args:
        text: The input text to capitalize.

    Returns:
        The text with the first letter of each word capitalized.
        Returns an empty string if text is None.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("open source development")
        'Open Source Development'
    """
    if text is None:
        return ""
    return text.title()
