'''
"Error: Device must be calibrated before first use.
Frequency drift detected. Cannot maintain destination lock."

Starting with a frequency of zero, what is the resulting frequency
after all of the changes in frequency have been applied?
'''

starting_freq = 0

with open('input.txt') as input_file:
    for frequency_change in input_file.read().splitlines():
        starting_freq += int(frequency_change)

print(starting_freq)
