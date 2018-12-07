'''
To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter
and then separately counting those with exactly three of any letter.

You can multiply those two counts together to get a rudimentary checksum
and compare it to what your device predicts.

What is the checksum for your list of box IDs?
'''


def get_frequency_dict(sequence):
    '''
    Returns a dictionary where keys are elements of the sequence
    and the values are the occurrences of elements in the sequence.
    '''
    freq_dict = {}
    for i in sequence:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    return freq_dict


def get_letter_frequency_bool(input_string, n):
    '''
    Returns the boolean value True if any letter in input_string has exactly n
    counts and False otherwise
    '''
    input_dict = get_frequency_dict(input_string)
    return True if n in input_dict.values() else False


def get_checksum(input_list):
    '''
    Returns the checksum where the checksum is the product of the
    number of strings with letters that appear exactly twice and the
    number of strings with letters that appear exactly thrice,
    given an input list
    '''
    letter_appears_twice_count = 0
    letter_appears_thrice_count = 0
    for string in input_list:
            if get_letter_frequency_bool(string, 2):
                letter_appears_twice_count += 1
            if get_letter_frequency_bool(string, 3):
                letter_appears_thrice_count += 1
    checksum = letter_appears_twice_count * letter_appears_thrice_count
    return(checksum)


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split()
        print(
            f'''The checksum for the list of box IDs is {
                get_checksum(input_list)
            }'''
        )

if __name__ == '__main__':
    main()
