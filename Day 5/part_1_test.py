import pytest
from part_1 import react_loop


def test_part_1():
    polymer_test = 'dabAcCaCBAcCcaDA'
    output_polymer = react_loop(polymer_test)
    assert output_polymer == 'dabCBAcaDA'
    assert len(output_polymer) == 10
