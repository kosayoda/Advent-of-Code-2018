'''
One of the unit types is causing problems;
it's preventing the polymer from collapsing as much as it should.

Your goal is to figure out which unit type is causing the most problems,
remove all instances of it (regardless of polarity),
fully react the remaining polymer, and measure its length.

What is the length of the shortest polymer you can produce by
removing all units of exactly one type and fully reacting the result?
'''

from part_1 import react_loop


def remove_unit_type(polymer, unit_type):
    '''
    Returns a polymer with all instances of the given unit type removed
    '''
    polymer = polymer.replace(unit_type, '').replace(unit_type.upper(), '')
    return polymer


def improve_polymer(polymer, unit_types):
    '''
    Returns a dictionary where every key is a unit type and the value is the
    length of polymer with unit type removed after full reaction, given the
    polymer and a string containing all the unit types
    '''
    polymer_dict = {}
    for unit_type in unit_types:
        final_polymer = react_loop(remove_unit_type(polymer, unit_type))
        polymer_dict[unit_type] = len(final_polymer)
    return polymer_dict


def get_shortest_polymer_length(input_dict):
    '''
    Returns the length of the shortest polymer that can be produced, given
    a dictionary where keys are unit types to be removed and value is the length
    of polymer with unit type removed after full reaction
    '''
    return min(input_dict.values())


def main():
    with open('input.txt') as input_file:
        polymer = input_file.read().strip()

    unit_types = 'abcdefghijklmnopqrstuvwxyz'
    polymer_dict = improve_polymer(polymer, unit_types)
    shortest_polymer_length = get_shortest_polymer_length(polymer_dict)
    print(
        'The length of the shortest polymer produced by removing all units '
        f'''of exactly one type and fully reacting the result is {
            shortest_polymer_length
        }'''
    )

if __name__ == '__main__':
    main()
