import pytest
from main import first_substr


def test_single_occurrence():
    assert first_substr("bonvanille", "o") == "onv"


def test_twice_occurrence():
    assert first_substr("bonbonvanille", "o") == "onb"


def test_upper_letter():
    assert first_substr("Bonbonvanille", "B") == "Bon"


def test_occurrence_at_end():
    assert first_substr("bonbonvanille", "e") is None


def test_int_input():
    assert first_substr("bonbonvanille", 10) is None


def test_multiple_char_input():
    assert first_substr("bonbonvaille", "on") is None


def test_empty_word():
    assert first_substr("", "o") is None


def test_empty_char():
    assert first_substr("bonbonvaille", "") is None


def test_empty():
    assert first_substr("", "") is None