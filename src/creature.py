import random
import math
from neural_network import NeuralNetwork


class Creature:
    def __init__(self, x, y, grid_size):
        self.x = x
        self.y = y
        self.grid_size = grid_size
        self.direction = random.randint(0, 7)
        self.genome = "".join(
            [format(random.randint(0, 16**8 - 1), "08x") for _ in range(4)]
        )
        self.brain = NeuralNetwork(self.genome)
        self.color = self.genome_to_color()

    def genome_to_color(self):
        return tuple(int(self.genome[i: i + 2], 16) for i in (0, 2, 4))

    def move(self, grid):
        forward_x = (
            self.x + round(math.cos(self.direction * math.pi / 4))
        ) % self.grid_size
        forward_y = (
            self.y + round(math.sin(self.direction * math.pi / 4))
        ) % self.grid_size
        density = sum(
            1
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if grid[(forward_y + dy) % self.grid_size][
                (forward_x + dx) % self.grid_size
            ]
            is not None
        )

        outputs = self.brain.activate([density / 9])

        if outputs[0] > 0.5:
            self.x = (self.x + 1) % self.grid_size
        elif outputs[1] > 0.5:
            self.direction = random.randint(0, 7)
            self.x = (
                self.x + round(math.cos(self.direction * math.pi / 4))
            ) % self.grid_size
            self.y = (
                self.y + round(math.sin(self.direction * math.pi / 4))
            ) % self.grid_size
