"""tests pour l'API publique du package"""

import textutils


def test_all_exports_are_functions():
    for name in textutils.__all__:
        assert callable(getattr(textutils, name))


def test_all_matches_module_attributes():
    # seules les fonctions publiques sont dans __all__
    public = [
        name
        for name in dir(textutils)
        if not name.startswith("_") and callable(getattr(textutils, name))
    ]
    assert sorted(textutils.__all__) == sorted(public)


def test_version_is_exposed():
    assert textutils.__version__ == "0.3.0"
