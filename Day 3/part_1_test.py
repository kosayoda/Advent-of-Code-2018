import pytest
from part_1 import Claim, claim_parser, find_overlapped_inches

list_test = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

claim_string_test = '#123 @ 3,2: 5x4'


claim_1 = Claim(claim_parser(list_test[0]))
claim_2 = Claim(claim_parser(list_test[1]))
claim_3 = Claim(claim_parser(list_test[2]))


def test_claim_parser():
    assert claim_parser(claim_string_test) == (123, 3, 2, 5, 4)


def test_claim():
    assert claim_1.points == {
        (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 3), (4, 4), (4, 5), (4, 6),
    }

    assert claim_2.points == {
        (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 1), (4, 2), (4, 3), (4, 4),
        (5, 1), (5, 2), (5, 3), (5, 4),
        (6, 1), (6, 2), (6, 3), (6, 4),
    }
    assert claim_3.points == {
        (5, 5), (5, 6),
        (6, 5), (6, 6)
    }


def test_find_overlapped_inches():
    assert find_overlapped_inches(list_test) == 4
