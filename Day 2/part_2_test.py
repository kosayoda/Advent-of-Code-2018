import pytest
from part_2 import get_one_diff_strings, find_similar_chars

list_test = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def test_get_one_diff_strings():
    string_1, string_2 = get_one_diff_strings(list_test)
    assert (string_1, string_2) == ('fghij', 'fguij')


def test_find_similar_chars():
    assert find_similar_chars("fghij", "fguij") == "fgij"
