from src.services.string_service import capitalize


def test_cap_classic():
    assert capitalize('hello Jean !') == 'Hello jean !'


def test_cap_int():
    assert capitalize(2) == 2


def test_cap_empty():
    assert capitalize("") == ""
