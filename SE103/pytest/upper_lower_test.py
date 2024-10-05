import pytest
from main import upper_lower


def test_lower_letters():
    assert not upper_lower("lowlow")


def test_upper_in_middle():
    assert upper_lower("blaBla")


def test_upper_lower_at_end():
    assert upper_lower("blabLa")


def test_upper_at_end():
    assert not upper_lower("blA")


def test_upper_at_start():
    assert upper_lower("Bla")


def test_upper_letter():
    assert not upper_lower("BLA")


def test_empty():
    assert not upper_lower("")
