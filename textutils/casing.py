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


def snake_case(text: str) -> str:
    """Convert a string to snake_case.

    Words are separated by underscores and converted to lowercase.
    Existing separators (spaces, hyphens, camelCase boundaries) are
    normalized to underscores.

    Args:
        text: The input text to convert.

    Returns:
        The text in snake_case format. Returns an empty string if text is None.

    Examples:
        >>> snake_case("Hello World")
        'hello_world'
        >>> snake_case("hello-world")
        'hello_world'
        >>> snake_case("HelloWorld")
        'hello_world'
    """
    if text is None:
        return ""
    # Replace separators and camelCase boundaries with underscores
    import re

    text = re.sub(r"[\s\-]+", "_", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    return text.lower().strip("_")


def camel_case(text: str) -> str:
    """Convert a string to camelCase.

    The first word is lowercase and subsequent words are capitalized.
    Existing separators (spaces, hyphens, underscores) are removed.

    Args:
        text: The input text to convert.

    Returns:
        The text in camelCase format. Returns an empty string if text is None.

    Examples:
        >>> camel_case("hello world")
        'helloWorld'
        >>> camel_case("open-source development")
        'openSourceDevelopment'
        >>> camel_case("hello_world")
        'helloWorld'
    """
    if text is None:
        return ""
    # Normalize separators to spaces, then title-case and join
    import re

    words = re.split(r"[\s\-_]+", text.strip())
    if not words:
        return ""
    first = words[0].lower()
    rest = [w.capitalize() for w in words[1:] if w]
    return first + "".join(rest)
