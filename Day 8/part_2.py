'''
The second check is slightly more complicated:
You need to find the value of the root node.

If a node has no child nodes, its value is the sum of its metadata entries.
However, if a node does have child nodes, the metadata entries become indexes
which refer to those child nodes. The value of this node is the sum of the
values of the child nodes referenced by the metadata entries.

What is the value of the root node?
'''


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata


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


def get_sum_value(node):
    if node.children:
        value = 0
        for index in node.metadata:
            if index <= len(node.children):
                value += get_sum_value(node.children[index - 1])
        return value
    else:
        return sum(node.metadata)

if __name__ == '__main__':
    with open('input.txt') as input_file:
        input_list = input_file.read().strip().split(' ')

    position = 0
    array = [int(i) for i in input_list]
    Tree = recurse()

    print(
        f'The value of the root node is {get_sum_value(Tree)}'
    )
