'''
You discover a dial on the side of the device; it seems to let you select a
square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total
power.Identify this square by including its size as a third parameter after the
top-left coordinate.

What is the X,Y,size identifier of the square with the largest total power?
'''

grid = [
    [0 for _ in range(300)] for _ in range(300)
]

serial_num = 1718
for y, line in enumerate(grid):
    for x, _ in enumerate(line):
        rack_id = x + 10
        power_level = (rack_id * y + serial_num) * rack_id
        power_level = int(str(power_level)[-3]) - 5
        grid[y][x] = power_level

power_list = []
for N in range(1, 21):  # Only testing 1-21, squares of >21 unlikely
    print(N)
    for y in range(301 - N):
        for x in range(301 - N):
            total_power = 0
            for i in range(N):
                for j in range(N):
                    total_power += grid[y + i][x + j]
            if total_power > 0:
                power_list.append(
                    ((x, y), N, total_power)
                )
    power_list = [max(power_list, key=lambda i: i[2])]

(max_x, max_y), size, max_power = max(power_list, key=lambda i: i[2])

print(
    'The coordinate of the top-left cell of the square with largest power is '
    f'{max_x},{max_y} '
    f'with a power of {max_power} and a size of {size}'
)