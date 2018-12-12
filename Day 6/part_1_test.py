import pytest
from part_1 import initialize_grid, closest_coordinate, find_finite_coordinates
from part_1 import get_largest_area

list_test = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9),
]


def test_part_1():
    grid = closest_coordinate(initialize_grid(list_test), list_test)
    coordinates = find_finite_coordinates(grid)
    assert get_largest_area(grid, coordinates) == 17
