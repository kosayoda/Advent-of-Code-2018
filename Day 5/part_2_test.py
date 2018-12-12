import pytest
from part_2 import remove_unit_type, improve_polymer, get_shortest_polymer_length

polymer_test = 'dabAcCaCBAcCcaDA'


def test_remove_unit_type():
    assert remove_unit_type(polymer_test, 'a') == 'dbcCCBcCcD'
    assert remove_unit_type(polymer_test, 'b') == 'daAcCaCAcCcaDA'
    assert remove_unit_type(polymer_test, 'c') == 'dabAaBAaDA'
    assert remove_unit_type(polymer_test, 'd') == 'abAcCaCBAcCcaA'


def test_improve_polymer():
    assert improve_polymer(polymer_test, 'abcd') == {
        'a': 6,
        'b': 8,
        'c': 4,
        'd': 6,
    }


def test_shortest_polymer_length():
    assert get_shortest_polymer_length(
        improve_polymer(polymer_test, 'abcd')
    ) == 4
