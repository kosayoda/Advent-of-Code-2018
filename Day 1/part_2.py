'''
You notice that the device repeats the same frequency change list over and over.
To calibrate the device,you need to find the first frequency it reaches twice.

What is the first frequency your device reaches twice?
'''

from itertools import cycle


def retrieve_repeat(input_list):
    '''
    Returns the first frequency reached twice after frequency changes from
    the input list
    '''
    starting_freq = 0
    seen_freq = {0}  # Contains reached frequencies
    for freq_change in cycle(input_list):
        starting_freq += int(freq_change)
        if starting_freq in seen_freq:
            return starting_freq
        seen_freq.add(starting_freq)


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split()
        print(
            f'''The first frequency the device will reach twice is {
                retrieve_repeat(input_list)
            }'''
        )

if __name__ == '__main__':
    main()
