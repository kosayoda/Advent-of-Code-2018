'''
While the very latest in 1518 alchemical technology might have solved their
problem eventually, you can do better.
You scan the chemical composition of the suit's material and discover that
it is formed by extremely long polymers.

The polymer is formed by smaller units which, when triggered,
react with each other such that two adjacent units of the same type and
opposite polarity are destroyed.

How many units remain after fully reacting the polymer you scanned?
'''


def react(polymer):
    '''
    Given a polymer string, removes two adjacent characters if they are the same
    character but in opposite cases
    Removes: aA, Aa
    Does not remove: aa, AA, aB, Ba
    '''
    for char_1, char_2 in zip(polymer, polymer[1:]):
        if char_1.lower() == char_2.lower() and char_1 != char_2:
            polymer = polymer.replace(f'{char_1}{char_2}', '', 1)
    return polymer


def react_loop(polymer):
    '''
    Given a polymer string, reacts repeatedly until no reaction occurs,
    returns the polymer string
    '''
    old_polymer = polymer
    while True:
        new_polymer = react(old_polymer)
        if new_polymer == old_polymer:
            return new_polymer
        else:
            old_polymer = new_polymer


def main():
    with open('input.txt') as input_file:
        polymer = input_file.read().strip()

    final_polymer = react_loop(polymer)
    print(
        f'''The units remaining after fully reacting the polymer is {
            len(final_polymer)
        } units.'''
    )

if __name__ == '__main__':
    main()
