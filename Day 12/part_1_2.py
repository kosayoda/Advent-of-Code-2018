'''
After exploring a little, you discover a long tunnel that contains a row of
small pots as far as you can see to your left and right.

It's not clear what these plants are for, but you're sure it's important, so
you'd like to make sure the current configuration of plants is sustainable by
determining what will happen after 20 generations.

After 20 generations, what is the sum of the numbers of all pots which contain
a plant?
'''


class Node:
    def __init__(self, data, index, _prev, _next):
        self.data = data
        self.index = index
        self.prev = _prev
        self.next = _next

    def __str__(self):
        return self.data

    def get_set_of_five(self):
        '''
        Return list of two nodes to the left, itself and two nodes to the right
        '''

        five_set = []

        if self == pots.head:
            five_set.append('..')
        elif self.index == pots.head.index + 1:
            five_set.append('.')
            five_set.append(self.prev.data)
        else:
            five_set.append(f'{self.prev.prev.data}{self.prev.data}')

        five_set.append(pot.data)

        if self == pots.tail:
            five_set.append('..')
        elif self.index == pots.tail.index - 1:
            five_set.append('.')
            five_set.append(self.next.data)
        else:
            five_set.append(f'{self.next.data}{self.next.next.data}')

        return ''.join(five_set)


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.current_node = None

    def __str__(self):
        current_node = self.head
        data_repr = []
        index_repr = []
        while True:
            try:
                data_repr.append(current_node.data)
                index_repr.append(str(current_node.index).zfill(2))
                current_node = current_node.next
            except:
                break
        return f'{"  ".join(data_repr)}\n{" ".join(index_repr)}'

    def __len__(self):
        return self.count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, data, index=None):
        if self.head is None:
            if index is None:
                new_node = Node(data, 0, None, None)
            else:
                # Preserve index of pot in previous generation
                new_node = Node(data, index, None, None)
            self.head = self.tail = new_node
        else:
            new_node = Node(data, self.tail.index + 1, None, None)

            new_node.prev = self.tail
            new_node.next = None

            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def appendleft(self, data):
        if self.head is None:
            new_node = Node(data, 0, None, None)
            self.head = self.tail = new_node
        else:
            new_node = Node(data, self.head.index - 1, None, None)

            new_node.next = self.head
            new_node.prev = None

            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def refresh(self):
        # Because pots besides first and last plant may grow in next generation
        if self.head.data == '#':
            self.appendleft('.')
            self.appendleft('.')

        if self.tail.data == '#':
            self.append('.')
            self.append('.')


test_initial_state = '#..#.#..##......###...###'

test_notes = [
    '...## => #',
    '..#.. => #',
    '.#... => #',
    '.#.#. => #',
    '.#.## => #',
    '.##.. => #',
    '.#### => #',
    '#.#.# => #',
    '#.### => #',
    '##.#. => #',
    '##.## => #',
    '###.. => #',
    '###.# => #',
    '####. => #'
]

with open('input.txt') as input_file:
    input_list = input_file.read().split('\n')

initial_state = input_list[0][15:]
notes = input_list[2:-1]

note_dict = dict()
for note in notes:
    # Notes are keys with value being # for plant and . for no plant
    note_dict[note[:5]] = note[-1]

pots = DLinkedList()
for i in initial_state:
    # Add pots in initial state to a DLinkedList
    pots.append(i)

total_generations = 20  #50000000000

last_sum = 0

for generation in range(1, total_generations + 1):
    if not generation % 10:
        print(f'\nCurrently at Generation {generation}')
    pots.refresh()
    new_gen = DLinkedList()  # Temporary pots for next_generation
    for pot in pots:
        pots_set = pot.get_set_of_five()
        try:
            new_gen.append(note_dict[''.join(pots_set)], pot.index)
        except KeyError:
            new_gen.append('.', pot.index)

    pots = new_gen

    sum_plants = 0
    for pot in pots:
        if pot.data == '#':
            sum_plants += pot.index

    print(
        f'''Current sum: {sum_plants}, difference with last sum: {
            (sum_plants - last_sum)
        }'''
    )
    last_sum = sum_plants

print()
print(
    f'''After 20 generations, the sum of numbers of pots that have plants is {
        last_sum
    }'''
)
print()
print(
    f'''After 50000000000 generations, the sum becomes {
        (50000000000 - 195) * 45 + 8895
    } because the sum increases by 45 plants every generation after 194'''
)