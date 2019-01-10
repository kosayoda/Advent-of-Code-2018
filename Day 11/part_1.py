'''
Tapping it once causes it to project a hologram of the situation: a 300x300
grid of fuel cells and their current power levels, some negative. You're not
sure what negative power means in the context of time travel, but it can't be
good.

Your goal is to find the 3x3 square which has the largest total power.
The square must be entirely within the 300x300 grid.
Identify this square using the X,Y coordinate of its top-left fuel cell.

What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the
largest total power?
'''

grid = [
    [0 for _ in range(300)] for _ in range(300)
]

serial_num = 1718
# Initialize grid with powerlevels
for y, line in enumerate(grid):
    for x, _ in enumerate(line):
        rack_id = x + 10
        power_level = (rack_id * y + serial_num) * rack_id
        power_level = int(str(power_level)[-3]) - 5
        grid[y][x] = power_level

power_list = []
for y in range(298):
    for x in range(298):
        total_power = 0
        total_power += sum((
            grid[y][x], grid[y][x + 1], grid[y][x + 2],
            grid[y + 1][x], grid[y + 1][x + 1], grid[y + 1][x + 2],
            grid[y + 2][x], grid[y + 2][x + 1], grid[y + 2][x + 2]
        ))
        power_list.append(
            ((x, y), total_power)
        )

(max_x, max_y), max_power = max(power_list, key=lambda i: i[1])

print(
    'The coordinate of the top-left cell of the square with largest power is '
    f'{max_x},{max_y} '
    f'with a power of {max_power}'
)