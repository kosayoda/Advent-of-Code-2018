'''
"Failed to start navigation system. Could not read software license file."

The navigation system's license file consists of a list of numbers.
The numbers define a data structure which, when processed, produces some kind
of tree that can be used to calculate the license number.

A node consists of:
    A header, which is always exactly two numbers:
        The quantity of child nodes.
        The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).

What is the sum of all metadata entries?
'''


class Node:
    def __init__(self, children, metadata):
        self.children = children  #Contains child Node objects
        self.metadata = metadata  #Contains metadata values


def get_value():
    '''
    Move along the array in one direction and return the value at current
    position
    '''
    global position
    if position == len(array):
        return None
    value = array[position]
    position += 1
    return value


def recurse():
    '''
    Creates a Node object by recursively going down the array
    '''
    child_nodes = get_value()
    num_metadata = get_value()

    children = []
    for _ in range(child_nodes):
        children.append(recurse())

    metadata = []
    for _ in range(num_metadata):
        metadata.append(get_value())

    return Node(children, metadata)


def get_sum_metadata(node):
    return sum(node.metadata) + sum(
        [get_sum_metadata(child_node) for child_node in node.children]
    )

if __name__ == '__main__':
    with open('input.txt') as input_file:
        input_list = input_file.read().strip().split(' ')

    position = 0
    array = [int(i) for i in input_list]
    Tree = recurse()

    print(
        f'The sum of all metadata entries is {get_sum_metadata(Tree)}'
    )