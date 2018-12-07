'''
Each Elf has made a claim about which area of fabricwould be ideal for
Santa's suit.

A claim like #123 @ 3,2: 5x4 means that claim ID 123
specifies a rectangle 3 inches from the left edge, 2 inches from the top edge,
5 inches wide, and 4 inches tall.

How many square inches of fabric are within two or more claims?
'''

import re
from itertools import combinations, product


class Claim():
    def __init__(self, params):
        '''
        Given parameters from claim_parser, create a set of all points
        occupied by the claim
        '''
        self.claim_id, self.col, self.row, self.width, self.height = params

        self.x_values = [self.col + i for i in range(self.width)]
        self.y_values = [self.row + i for i in range(self.height)]
        self.points = set(i for i in product(self.x_values, self.y_values))


def claim_parser(claim):
    '''
    Given a string containing a claim, returns a tuple of
    claim id, column number, row number, width of claim, height of claim
    '''
    claim_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    m = re.match(claim_regex, claim)
    claim_id, col, row, width, height = m.groups()

    return int(claim_id), int(col), int(row), int(width), int(height)


def objectify_claims(input_list):
    '''
    Returns a list of claim objects, given a list of claim strings
    '''
    return [Claim(claim_parser(i)) for i in input_list]


def check_overlap(claim_1, claim_2):
    '''
    Returns a set containing overlapping coordinates between two claims,
    given two claim objects
    '''
    return claim_1.points & claim_2.points


def find_overlapped_inches(input_list):
    '''
    Returns the total number of overlapped inches given a list of claim strings
    '''
    total_overlapped_inches = set()
    claim_list = objectify_claims(input_list)
    for claim_1, claim_2 in combinations(claim_list, 2):
        overlapped_inches = check_overlap(claim_1, claim_2)
        for i in overlapped_inches:
            total_overlapped_inches.add(i)

    return len(total_overlapped_inches)


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
        overlapped_inches = find_overlapped_inches(
            input_list
        )
        print(
            f'''Number of square inches within two or more claims is {
                    overlapped_inches
                }'''
        )

if __name__ == '__main__':
    main()
