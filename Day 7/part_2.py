'''
"The sun will set soon; it'll go faster if we work together."
Now, you need to account for multiple people working on steps simultaneously.
If multiple steps are available, workers should still begin them in
alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter:
A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds,
while step Z takes 60+26=86 seconds. No time is required between steps.

With 5 workers and the 60+ second step durations described above,
how long will it take to complete all of the steps?
'''

from collections import defaultdict


def get_time(step):
    '''
    Returns time needed for each step
    '''
    alphabet_string = '0abcdefghijklmnopqrstuvwxyz'
    return alphabet_string.index(step.lower()) + 60


def get_work(frontier, worker):
    '''
    Given the frontier and a worker, assigns work to the worker if there is work
    '''
    if frontier:
        work = sorted(frontier)[0]  # Sort frontier by lexicographic order
        worker[0], worker[1] = get_time(work), work
        frontier.remove(work)
    return frontier, worker


def work_done(frontier, traversed, edges, work):
    '''
    Updates the frontier and traversed if a job is done
    '''

    traversed.append(work)

    available_nodes = [
        node_2 for node_1, node_2 in edges if node_1 == work
    ]  # Nodes that have the current node as a prerequisite

    for node in available_nodes:
        '''
        Node is blocked if the node has a prerequisite which is not the current
        node and the prerequisite has not been traversed
        '''
        node_blocked = any(
            node_1 for node_1, node_2 in edges if (node_2 == node) and
            (node_1 != work) and (node_1 not in traversed)
        )
        if not node_blocked:
            frontier.add(node)

    return frontier, traversed


def main(input_list, num_workers):
    edges = []

    for i in input_list:
        current_node = i[5]
        next_node = i[-12]
        edges.append((current_node, next_node))

    frontier = set(current_node for current_node, _ in edges) - set(
        next_node for _, next_node in edges
    )  # Any node that has no prerequisite node

    traversed = []  # Nodes we have gone through

    workers = defaultdict(list)

    time = 0

    for i in range(num_workers):
        workers[i] = [0, None]

    while frontier or any([workers[i][1] for i in workers]):
        # While frontier isn't empty or workers have work to do
        for i in workers:
            if workers[i][0] == 0 and workers[i][1] is None:
                # Get work for workers without job
                frontier, workers[i] = get_work(frontier, workers[i])
            elif workers[i][0] == 0 and workers[i][1] is not None:
                # Mark work as done for workers who have finished
                frontier, traversed = work_done(frontier, traversed, edges, workers[i][1])
                workers[i][1] = None

        for i in workers:
            if workers[i][0] == 0 and workers[i][1] is None:
                # Assign work for workers who just finished work
                frontier, workers[i] = get_work(frontier, workers[i])
            if workers[i][0] > 0:
                # Reduce work time for workers working
                workers[i][0] -= 1

        if not frontier and not any([workers[i][1] for i in workers]):
            # Break early if everything is finished
            break

        time += 1

    print(
        f'''The order in which the steps should be completed is {
            ''.join(traversed)
        }'''
    )
    print(
        f'It will take {time} seconds to complete all the steps'
    )

    #return time  #For testing purposes

if __name__ == '__main__':
    with open('input.txt') as input_file:
        input_list = input_file.read().split('\n')
    main(input_list, 5)