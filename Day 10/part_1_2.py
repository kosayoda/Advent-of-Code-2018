'''
You can see these points of light floating in the distance,
and record their position in the sky and their velocity, the relative change
in position per second.

Rather than wait, you decide to fast-forward the process and calculate what the
points will eventually spell.

What message will eventually appear in the sky?

Exactly how many seconds would they have needed to wait for that message to
appear?
'''

import re

test_list = [
    'position=< 9,  1> velocity=< 0,  2>',
    'position=< 7,  0> velocity=<-1,  0>',
    'position=< 3, -2> velocity=<-1,  1>',
    'position=< 6, 10> velocity=<-2, -1>',
    'position=< 2, -4> velocity=< 2,  2>',
    'position=<-6, 10> velocity=< 2, -2>',
    'position=< 1,  8> velocity=< 1, -1>',
    'position=< 1,  7> velocity=< 1,  0>',
    'position=<-3, 11> velocity=< 1, -2>',
    'position=< 7,  6> velocity=<-1, -1>',
    'position=<-2,  3> velocity=< 1,  0>',
    'position=<-4,  3> velocity=< 2,  0>',
    'position=<10, -3> velocity=<-1,  1>',
    'position=< 5, 11> velocity=< 1, -2>',
    'position=< 4,  7> velocity=< 0, -1>',
    'position=< 8, -2> velocity=< 0,  1>',
    'position=<15,  0> velocity=<-2,  0>',
    'position=< 1,  6> velocity=< 1,  0>',
    'position=< 8,  9> velocity=< 0, -1>',
    'position=< 3,  3> velocity=<-1,  1>',
    'position=< 0,  5> velocity=< 0, -1>',
    'position=<-2,  2> velocity=< 2,  0>',
    'position=< 5, -2> velocity=< 1,  2>',
    'position=< 1,  4> velocity=< 2,  1>',
    'position=<-2,  7> velocity=< 2, -2>',
    'position=< 3,  6> velocity=<-1, -1>',
    'position=< 5,  0> velocity=< 1,  0>',
    'position=<-6,  0> velocity=< 2,  0>',
    'position=< 5,  9> velocity=< 1, -2>',
    'position=<14,  7> velocity=<-2,  0>',
    'position=<-3,  6> velocity=< 2, -1>',
]


def update_points(array):
    new_array = []
    for x, y, xv, yv in array:
        new_array.append((x + xv, y + yv, xv, yv))

    return new_array


with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')

point_list = []

for line in input_list:
    x, y, xv, yv = map(int, re.findall(r'-*\d+', line))
    point_list.append((x, y, xv, yv))

for time in range(100000):
    min_x = min([x for x, *_ in point_list])
    max_x = max([x for x, *_ in point_list])

    min_y = min([y for _, y, *_ in point_list])
    max_y = max([y for _, y, *_ in point_list])

    if max_x - min_x < 100 and max_y - min_y < 100:
        # Within range of coherent words
        grid = [
            ['.' for i in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)
        ]

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):

                if (x, y) in [(x, y) for x, y, *_ in point_list]:
                    grid[max_y - y][max_x - x] = '#'

        for y in reversed(grid):
            print(''.join(reversed(y)))
        print(f'The time taken for the above message is {time} seconds.')

    point_list = update_points(point_list)