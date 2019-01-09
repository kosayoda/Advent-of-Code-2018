from collections import deque, defaultdict


number_of_players = 459
last_marble = 7179000

circle = deque([0])
score_dictionary = defaultdict(int)

for next_marble in range(1, last_marble + 1):
    current_player = next_marble % number_of_players

    if next_marble % 23:  # Not divisible by 23
        circle.rotate(-1)
        circle.append(next_marble)
    else:  # Divisible by 23
        circle.rotate(7)
        score_dictionary[current_player] += next_marble + circle.pop()
        circle.rotate(-1)

print(
    f'The winning elf\'s score is {sorted(score_dictionary.values())[-1]}'
)