import pytest
from part_1 import time_parser, guard_parser, shift_parser
from part_1 import max_sleep_guard, minute_slept_most

timestamp_guard_test = '[1518-11-01 00:00] Guard #10 begins shift'
timestamp_time_test = '[1518-11-01 00:05] falls asleep'

record_test = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up',
]


def test_record_parser():
    assert time_parser(timestamp_time_test) == (
        1518, 11, 1, 00, 5
    )


def test_guard_parser():
    assert guard_parser(timestamp_guard_test) == '10'


def test_max_sleep_time():
    best_guard, max_time_asleep, asleep_minutes = max_sleep_guard(
        shift_parser(record_test)
    )
    print(max_sleep_guard(shift_parser(record_test)))
    assert best_guard == '10'
    assert max_time_asleep == 50
    assert minute_slept_most(asleep_minutes) == 24
    assert int(best_guard) * minute_slept_most(asleep_minutes) == 240
