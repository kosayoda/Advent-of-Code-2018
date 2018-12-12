'''
On the other hand, if the coordinates are safe, maybe the best you can do is
try to find a region near as many coordinates as possible.

For each location, add up the distances to all of the given coordinates;
if the total of those distances is less than x, that location is within
the desired region.

What is the size of the region containing all locations which have a total
distance to all given coordinates of less than 10000?
'''

import numpy as np


def manhattan(p, q):
    '''
    Returns the manhattan distance between points p and q
    '''
    return sum(abs(a - b) for a, b in zip(p, q))


def coordinate_distances(grid, coordinate_list, safe_distance):
    '''
    Returns the number of points within safe distance from all coordinates given
    '''
    points_within_region = 0
    for (row, col), _ in np.ndenumerate(grid):
        total_dist = 0
        for i in coordinate_list:
            total_dist += manhattan((col, row), i)
        if total_dist < safe_distance:
            points_within_region += 1

    return points_within_region


def initialize_grid(coordinates):
    '''
    Returns a grid of zeroes from (0, 0) to the furthest coordinate from top
    left corner
    '''
    x, y = [i[0] for i in coordinates], [i[1] for i in coordinates]
    max_x, max_y = max(x), max(y)
    grid = np.zeros((max_y + 1, max_x + 1))

    return grid


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
    coordinate_list = []
    for i in input_list:
        x_val, y_val = i.split(", ")
        coordinate_list.append((int(x_val), int(y_val)))

    grid = initialize_grid(coordinate_list)

    print(
        'What is the size of the region containing all locations which ' +
        'have a total distance to all given coordinates of less than 10000 ' +
        f'is {coordinate_distances(grid, coordinate_list, 10000)}'
    )

if __name__ == '__main__':
    main()
