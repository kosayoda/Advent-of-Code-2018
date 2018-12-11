import pytest
from part_2 import retrieve_repeat

1_test = [+1, -1]
2_test = [+3, +3, +4, -2, -4]
3_test = [-6, +3, +8, +5, -6]
4_test = [+7, +7, -2, -7, -4]


def test_answer():
    assert retrieve_repeat(1_test) == 0
    assert retrieve_repeat(2_test) == 10
    assert retrieve_repeat(3_test) == 5
    assert retrieve_repeat(4_test) == 14
