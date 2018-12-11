'''
If you can figure out the guard most likely to be asleep at a specific time,
you might be able to trick that guard into working tonight so you can have
the best chance of sneaking in.

Find the guard that has the most minutes asleep.
What minute does that guard spend asleep the most?

What is the ID of the guard you chose multiplied by the minute you chose?
'''

import re
import datetime
from collections import defaultdict


def time_parser(input_string):
    '''
    Returns a tuple containing the date and time given a timestamp string
    '''
    record_regex = re.compile(
        r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]'
    )
    m = re.match(record_regex, input_string)
    year, month, day, hour, minute = m.groups()
    return (
        int(year), int(month), int(day), int(hour), int(minute)
    )


def tuple_to_datetime(input_tuple):
    '''
    Returns a datetime object given a tuple containing the date and time
    '''
    return datetime.datetime(*input_tuple)


def guard_parser(input_string):
    '''
    Returns a string containing the guard id given a timestamp string
    '''
    guard_regex = re.compile(r'#(\d+)')
    m = re.search(guard_regex, input_string)
    return m.group(1)


def shift_parser(input_list):
    '''
    Returns a dictionary where keys are guards and values are a list where
    first element is the time asleep and subsequent elements are a tuple of
    sleep and awake minutes, given a sorted list of timestamps
    '''
    record_dict = defaultdict(lambda: [0])
    for line in input_list:
        if line.endswith('shift'):
            guard_id = guard_parser(line)
        elif line.endswith('asleep'):
            sleep_time = time_parser(line)
        elif line.endswith('up'):
            wake_time = time_parser(line)
            wake_object = tuple_to_datetime(wake_time)
            sleep_object = tuple_to_datetime(sleep_time)

            timedelta_asleep = wake_object - sleep_object
            time_asleep = timedelta_asleep.total_seconds() / 60
            record_dict[guard_id][0] += time_asleep

            record_dict[guard_id].append(
                (sleep_time[4], wake_time[4])
            )
        else:
            pass
    return record_dict


def max_sleep_guard(input_dict):
    '''
    Returns the guard with longest sleep time and subsequent sleep and wake
    minutes, given a dictionary with different guard as keys
    '''
    best_guard = max(input_dict, key=input_dict.get)
    return best_guard, input_dict[best_guard][0], input_dict[best_guard][1:]


def minute_slept_most(input_list):
    '''
    Returns the minute slept most by a guard, given a list where each tuple
    has the sleep minute followed by the awake minute
    '''
    minute_dict = {}
    for sleep, wake in input_list:
        for i in range(sleep, wake):
            minute_dict[i] = minute_dict.get(i, 0) + 1
    return max(minute_dict, key=minute_dict.get)


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
        sorted_list = sorted(input_list)

        guard_dictionary = shift_parser(sorted_list)

        best_guard, max_time_asleep, asleep_minutes = max_sleep_guard(
            guard_dictionary
        )

        print(
            f'''The guard that slept the most on the job was Guard {
                best_guard
                }, and he slept for a total of {max_time_asleep} minutes.'''
        )
        print(
            f'''The minute Guard {best_guard} slept most was minute {
                minute_slept_most(asleep_minutes)
            }'''
        )
        print(
            f'''The ID of the guard multiplied by the minute is {
                int(best_guard) * minute_slept_most(asleep_minutes)
            }'''
        )

if __name__ == '__main__':
    main()
