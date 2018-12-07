import pytest
from part_2 import non_overlapping_claim

test_list = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]


def test_main():
    assert non_overlapping_claim(test_list).pop() == 3
