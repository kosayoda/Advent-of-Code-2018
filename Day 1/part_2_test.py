import pytest
from part_2 import retrieve_repeat

test1 = [+1, -1]
test2 = [+3, +3, +4, -2, -4]
test3 = [-6, +3, +8, +5, -6]
test4 = [+7, +7, -2, -7, -4]


def test_answer():
    assert retrieve_repeat(test1) == 0
    assert retrieve_repeat(test2) == 10
    assert retrieve_repeat(test3) == 5
    assert retrieve_repeat(test4) == 14
