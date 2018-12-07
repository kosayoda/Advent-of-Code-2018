'''
Amidst the chaos, you notice that exactly one claim doesn't overlap
by even a single square inch of fabric with any other claim.

What is the ID of the only claim that doesn't overlap?
'''

from part_1 import Claim, claim_parser, objectify_claims
from itertools import combinations


def overlaps(claim_1, claim_2):
    '''
    Returns a boolean True if claim_1 overlaps with claim_2 and False otherwise,
    given two claim objects
    '''
    return not claim_1.points.isdisjoint(claim_2.points)


def non_overlapping_claim(input_list):
    '''
    Returns the id of the non-overlapping claim given a list of claim strings
    '''
    overlapping_claims = set()

    claim_list = objectify_claims(input_list)
    for claim_1, claim_2 in combinations(claim_list, 2):
        if overlaps(claim_1, claim_2):
            overlapping_claims.add(claim_1.claim_id)
            overlapping_claims.add(claim_2.claim_id)

    return set(i for i in range(1, 1288)) - overlapping_claims


def main():
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
        print(
            f'''The ID of the only claim that doesn\'t overlap is {
                non_overlapping_claim(input_list).pop()
            }'''
        )

if __name__ == '__main__':
    main()
