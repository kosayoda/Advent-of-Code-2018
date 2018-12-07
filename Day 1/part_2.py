'''
You notice that the device repeats the same frequency change list over and over.
To calibrate the device,you need to find the first frequency it reaches twice.

What is the first frequency your device reaches twice?
'''

from itertools import cycle


def retrieve_repeat(input_list):
    starting_freq = 0
    seen_freq = {0}  # Contains reached frequencies
    for i in cycle(input_list):
        starting_freq += int(i)
        if starting_freq in seen_freq:
            return starting_freq
        seen_freq.add(starting_freq)

with open('input.txt') as input_file:
    input_list = input_file.read().split()
    output = retrieve_repeat(input_list)
    print(output)
