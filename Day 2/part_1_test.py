import pytest
from part_1 import get_letter_frequency_bool, get_checksum

list_test = [
    "abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"
]

letter_freq_bool_list = [
    (False, False), (True, True), (True, False),
    (False, True), (True, False), (True, False), (False, True),
]


def test_get_letter_frequency_bool():
    for i, string in enumerate(list_test):
        letter_appears_twice, letter_appears_thrice = letter_freq_bool_list[i]
        assert get_letter_frequency_bool(string, 2) == letter_appears_twice
        assert get_letter_frequency_bool(string, 3) == letter_appears_thrice


def test_get_checksum():
    assert get_checksum(list_test) == 12
