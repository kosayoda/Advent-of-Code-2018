"""
The instructions specify a series of steps and requirements about
which steps must be finished before others can begin.
Each step is designated by a single letter.

Your first goal is to determine the order in which the steps should be completed.
If more than one step is ready, choose the step which is first alphabetically.

In what order should the steps in your instructions be completed?
"""


def main(input_list):
    edges = []

    for i in input_list:
        current_node = i[5]
        next_node = i[-12]
        edges.append((current_node, next_node))

    frontier = set(current_node for current_node, _ in edges) - set(
        next_node for _, next_node in edges
    )  # Any node that has no prerequisite node

    traversed = []  # Nodes we have gone through

    while frontier:
        current_node = sorted(frontier)[0]  # Sort frontier by lexicographic order
        frontier.remove(current_node)
        traversed.append(current_node)

        available_nodes = [
            node_2 for node_1, node_2 in edges if node_1 == current_node
        ]  # Nodes that have the current node as a prerequisite

        for node in available_nodes:
            '''
            Node is blocked if the node has a prerequisite which is not the current
            node and the prerequisite has not been traversed
            '''
            node_blocked = any(
                node_1 for node_1, node_2 in edges if (node_2 == node) and
                (node_1 != current_node) and (node_1 not in traversed)
            )
            if not node_blocked:
                frontier.add(node)

    print(
        f'''The order in which the steps should be completed is {
            ''.join(traversed)
        }'''
    )

    #return ''.join(traversed)  #For testing purposes

if __name__ == '__main__':
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
    main(input_list)