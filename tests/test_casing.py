"""tests pour casing"""

import pytest

from textutils.casing import capitalize_words, snake_case, camel_case


@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world", "Hello World"),
        ("Hello World", "Hello World"),   # deja capitalise
        ("o'brien", "O'Brien"),           # l'apostrophe est geree
        ("123abc", "123Abc"),
        ("déjà vu", "Déjà Vu"),
        ("", ""),
        (None, ""),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Hello World", "hello_world"),
        ("hello-world", "hello_world"),
        ("hello_world", "hello_world"),
        ("helloWorld", "hello_world"),     # casse camel en entree
        ("hello  world", "hello_world"),   # espaces multiples
        ("  hello  ", "hello"),
        ("", ""),
        (None, ""),
    ],
)
def test_snake_case(text, expected):
    assert snake_case(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world", "helloWorld"),
        ("open source dev", "openSourceDev"),
        ("Hello World", "helloWorld"),
        ("hello-world", "helloWorld"),
        ("hello_world", "helloWorld"),
        ("hello", "hello"),          # un seul mot
        ("", ""),
        ("   ", ""),                 # que des espaces
        (None, ""),
    ],
)
def test_camel_case(text, expected):
    assert camel_case(text) == expected
