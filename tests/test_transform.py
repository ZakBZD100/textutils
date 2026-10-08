"""tests pour transform"""

import pytest

from textutils.transform import (
    word_count,
    character_count,
    reverse,
    slugify,
    word_frequency,
)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Hello World", 2),  # cas normal
        ("one", 1),  # un seul mot
        ("  hello   world  ", 2),  # espaces en trop
        ("hello\nworld\t!", 3),  # tabulations et sauts de ligne
        ("café naïve", 2),  # caracteres accentues
        ("   ", 0),  # que des espaces
        ("", 0),  # chaine vide
        (None, 0),  # texte absent
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Hello", 5),
        (" ", 1),  # l'espace compte
        ("", 0),
        ("café", 4),  # les accents comptent aussi
        (None, 0),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


def test_character_count_wrong_type():
    # un entier n'a pas de longueur
    with pytest.raises(TypeError):
        character_count(42)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Hello", "olleH"),
        ("racecar", "racecar"),  # palindrome
        ("ab", "ba"),
        ("", ""),
        (None, ""),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


def test_reverse_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Hello World", "hello-world"),
        ("Open Source!", "open-source"),
        ("Hello   World", "hello-world"),  # espaces multiples
        ("  spaces  everywhere  ", "spaces-everywhere"),
        ("a---b", "a-b"),  # tirets multiples
        ("Déjà Vu!", "déjà-vu"),  # les accents sont gardes
        ("hello_world", "helloworld"),  # le underscore disparait
        ("...", ""),  # rien de valide
        (None, ""),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world hello", {"hello": 2, "world": 1}),
        ("Hello hello HELLO", {"hello": 3}),  # ignore la casse
        ("hello, world! hello.", {"hello": 2, "world": 1}),  # ponctuation
        ("hello!!! ???", {"hello": 1}),  # mot sans lettres
        ("a\n\nb   a", {"a": 2, "b": 1}),  # sauts de ligne
        ("café café", {"café": 2}),  # accentues
        ("1 2 1", {"1": 2, "2": 1}),  # chiffres
        ("hello", {"hello": 1}),
        ("   ", {}),  # que des espaces
        ("!!! ???", {}),  # que de la ponctuation
        ("", {}),
        (None, {}),
    ],
)
def test_word_frequency(text, expected):
    assert word_frequency(text) == expected


def test_word_frequency_keeps_order():
    # l'ordre de premiere apparition est preserve
    assert list(word_frequency("b a b a").keys()) == ["b", "a"]
