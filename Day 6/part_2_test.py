import pytest
from part_2 import initialize_grid, coordinate_distances


def test_part_2():
    list_test = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]
    grid = initialize_grid(list_test)
    assert coordinate_distances(grid, list_test, 32) == 16
