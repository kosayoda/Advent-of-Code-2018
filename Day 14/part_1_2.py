"""
The Elves think their skill will improve after making a few recipes.

However, that could take ages; you can speed this up considerably by identifying
the scores of the ten recipes after that.

What are the scores of the ten recipes immediately after the number of recipes
in your puzzle input?
"""


class Scoreboard:
    def __init__(self, values):
        self.board = values

        self.elf_1 = 0
        self.elf_2 = 1

    def __str__(self):
        return f"Current board: {self.board}\nElf 1: {self.board[self.elf_1]}\nElf 2: {self.board[self.elf_2]}"

    def create_recipe(self):
        sum_recipes = self.board[self.elf_1] + self.board[self.elf_2]
        for i in str(sum_recipes):
            self.board.append(int(i))

    def get_new_recipe(self):
        self.elf_1 += (1 + self.board[self.elf_1]) % len(self.board)
        self.elf_1 = self.elf_1 % len(self.board)

        self.elf_2 += (1 + self.board[self.elf_2]) % len(self.board)
        self.elf_2 = self.elf_2 % len(self.board)

    def move_forward(self, n=1):
        for _ in range(n):
            self.create_recipe()
            self.get_new_recipe()

    def score_check(self, n):
        while len(self.board) < n + 10:
            self.move_forward()
        score = self.board[n : n + 10]
        return "".join(str(i) for i in score)

    def recipes_before_sequence(self, seq):
        """Move forward while the last len(seq) recipes are not seq"""
        target = [int(i) for i in str(seq)]
        seq_len = len(target)
        while True:
            if self.board[-seq_len:] == target:
                return len(self.board) - seq_len
            elif self.board[-seq_len - 1 : -1] == target:
                return len(self.board) - seq_len - 1
            self.move_forward()


N = 825_401

scoreboard = Scoreboard([3, 7])  # Part 1
print(f"The scores of ten recipes after {N} recipes is {scoreboard.score_check(N)}")

scoreboard_2 = Scoreboard([3, 7])  # Part 2
print(
    f"{scoreboard_2.recipes_before_sequence(N)} recipes appear on the scoreboard to the left of {N}"
)