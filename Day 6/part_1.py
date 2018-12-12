'''
"Situation critical," the device announces. "Destination indeterminate.
Chronal interference detected. Please specify new target coordinates."

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate
by counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite.
What is the size of the largest area that isn't infinite?
'''

import numpy as np
from itertools import count
from collections import Counter


def manhattan(p, q):
    '''
    Returns the manhattan distance between points p and q
    '''
    return sum(abs(a - b) for a, b in zip(p, q))


def initialize_grid(coordinates):
    '''
    Returns a grid where each coordinate in the list of coordinates is a unique
    number and the rest are zeroes
    '''
    x, y = [i[0] for i in coordinates], [i[1] for i in coordinates]
    max_x, max_y = max(x), max(y)
    grid = np.zeros((max_y + 1, max_x + 1))

    label_gen = count(1)
    for x, y in coordinates:
        grid[y][x] = label_gen.__next__()

    return grid


def closest_coordinate(grid, coordinate_list):
    '''
    Returns a grid where each coordinate is the nearest unique number coordinate
    and the coordinate is zero if two or more unique number coordinates have the
    same manhattan distance
    '''
    for (row, col), value in np.ndenumerate(grid):
        if value == 0:
            winner = [
                i for i in coordinate_list if (
                    manhattan((col, row), i) == min(
                        [manhattan((col, row), i) for i in coordinate_list]
                    )
                )
            ]
            winner_col, winner_row = winner[0]
            if len(winner) == 1:
                grid[row][col] = grid[winner_row][winner_col]
            else:
                grid[row][col] = 0
        else:
            pass
    return grid


def find_finite_coordinates(grid):
    '''
    Return the unique number if the coordinates represented by the unique number
    is finite
    '''
    finite_coordinates = set(np.unique(grid))
    border_slices = [
        grid[..., 0], grid[-1, ...], grid[0, ...], grid[..., -1]
    ]
    for i in border_slices:
        for j in set(np.unique(i)):
            finite_coordinates.discard(j)

    return finite_coordinates


def get_largest_area(grid, coordinates):
    '''
    Returns the largest area size in the given grid among given coordinates
    '''
    _, unique_index = np.unique(grid, return_inverse=True)
    counts = np.bincount(unique_index)
    return max([counts[int(i)] for i in coordinates])


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
    coordinate_list = []
    for i in input_list:
        x_val, y_val = i.split(", ")
        coordinate_list.append((int(x_val), int(y_val)))

    grid = initialize_grid(coordinate_list)
    grid = closest_coordinate(grid, coordinate_list)
    finite_coordinates = find_finite_coordinates(grid)

    print(
        f'''The size of the largest area that isn't infinite is {
            get_largest_area(grid, finite_coordinates)
        }'''
    )

if __name__ == '__main__':
    main()
