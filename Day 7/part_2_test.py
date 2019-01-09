import pytest
from part_2 import main

list_test = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]


def test_main():
    ''' Remember to change the time taken for each step in part_2 '''
    answer = main(list_test, 2)
    assert answer == 15