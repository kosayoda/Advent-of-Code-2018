'''
Of all guards, which guard is most frequently asleep on the same minute?

What is the ID of the guard you chose multiplied by the minute you chose?
'''

from collections import defaultdict
from part_1 import guard_parser, time_parser


def shift_parser(input_list):
    '''
    Returns a dictionary where keys are guards and values are a list of
    tuples of sleep and awake minutes, given a sorted list of timestamps.

    Element 0 and Element 1 of the list are placeholders for minute guard slept
    most and frequency of minute slept
    '''
    record_dict = defaultdict(lambda: [0, 0])  # [0, 0] are placeholders
    for line in input_list:
        if line.endswith('shift'):
            guard_id = guard_parser(line)
        elif line.endswith('asleep'):
            sleep_time = time_parser(line)
        elif line.endswith('up'):
            wake_time = time_parser(line)

            record_dict[guard_id].append(
                (sleep_time[4], wake_time[4])
            )
        else:
            pass
    return record_dict


def max_minute_and_freq(input_list):
    '''
    Returns the minute slept most by a guard and the frequency,
    given a list where each tuple has the sleep minute followed by
    the awake minute
    '''
    minute_dict = {}
    for sleep, wake in input_list:
        for i in range(sleep, wake):
            minute_dict[i] = minute_dict.get(i, 0) + 1
    return max(minute_dict, key=minute_dict.get), max(minute_dict.values())


def update_dict(input_dict):
    '''
    Returns an updated dictionary -->

    Given a dictionary in the format:
    {guard_id}: [placeholder, placeholder, (sleep, wake), (sleep,wake) ... ]
    returns a dictionary in the format:
    {guard_id}: [
        minute_slept_most, total_times_slept_that_minute, (sleep, wake), ...
    ]
    '''
    for guard, values in input_dict.items():
        minute_slept_most, minute_slept_most_freq = max_minute_and_freq(
            values[2:]
        )
        input_dict[guard][0] = minute_slept_most
        input_dict[guard][1] = minute_slept_most_freq
    return input_dict


def guard_slept_most_freq(input_dict):
    '''
    Returns the guard that slept and minute more than any other guard,
    that minute and how many times the guard slept on that minute
    '''
    best_guard = max(input_dict, key=lambda i: input_dict[i][1])
    return best_guard, input_dict[best_guard][0], input_dict[best_guard][1]


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
        sorted_list = sorted(input_list)

        guard_dictionary = update_dict(shift_parser(sorted_list))

        best_guard, minute_slept, minute_freq = guard_slept_most_freq(
            guard_dictionary
        )

        print(
            f'''The guard most frequently asleep on the same minute is Guard {
                best_guard
            }. He is most asleep on minute {
                minute_slept
            } and slept {minute_freq} times'''
        )
        print(
            f'''The ID of Guard {best_guard} multiplied by the minute is {
                int(best_guard) * minute_slept
            }'''
        )


if __name__ == '__main__':
    main()
