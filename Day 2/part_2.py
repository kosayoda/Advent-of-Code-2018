'''
Confident that your list of box IDs is complete,
you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one characterat the same
position in both strings.

What letters are common between the two correct box IDs?
'''


def get_one_diff_strings(input_list):
    '''
    Returns two strings with exactly one similar character given a list
    '''
    sorted_list = sorted(input_list)
    # Loops a, b -> b, c -> c, d -> d, e for [a, b, c, d, e]
    for string_1, string_2 in zip(sorted_list, sorted_list[1:]):
        # Compares each char in string_1 with string_2 and sum differences
        if sum(1 for a, b in zip(string_1, string_2) if a != b) == 1:
            return string_1, string_2


def find_similar_chars(string_1, string_2):
    '''
    Returns a string with the similar character removed, assuming the
    two input strings differ by exactly 1 character
    '''
    for index, pair in enumerate(zip(string_1, string_2)):
        char_1, char_2 = pair
        if char_1 != char_2:
            return string_1[:index] + string_1[index + 1:]


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split()
        string_1, string_2 = get_one_diff_strings(input_list)
        common_letters = find_similar_chars(string_1, string_2)
        print(common_letters)

if __name__ == '__main__':
    main()
