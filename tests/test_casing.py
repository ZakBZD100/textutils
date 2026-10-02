"""tests pour casing"""

from textutils.casing import capitalize_words, snake_case, camel_case


def test_capitalize():
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_deja():
    assert capitalize_words("Hello World") == "Hello World"

def test_snake_case():
    assert snake_case("Hello World") == "hello_world"

def test_snake_case_hyphen():
    assert snake_case("hello-world") == "hello_world"

def test_camel_case():
    assert camel_case("hello world") == "helloWorld"

def test_camel_case_multiple():
    assert camel_case("open source dev") == "openSourceDev"
