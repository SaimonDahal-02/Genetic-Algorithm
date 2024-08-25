import random
from creature import Creature
import pygame


class Grid:
    def __init__(self, width, height, num_creatures):
        self.width = width
        self.height = height
        self.creatures = []
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.populate(num_creatures)

    def populate(self, num_creatures):
        for _ in range(num_creatures):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.grid[y][x] is None:
                    creature = Creature(x, y, self.width)
                    self.grid[y][x] = creature
                    self.creatures.append(creature)
                    break

    def update(self):
        new_grid = [[None for _ in range(self.width)]
                    for _ in range(self.height)]
        for creature in self.creatures:
            old_x, old_y = creature.x, creature.y
            creature.move(self.grid)
            if new_grid[creature.y][creature.x] is None:
                new_grid[creature.y][creature.x] = creature
            else:
                creature.x, creature.y = old_x, old_y
                new_grid[old_y][old_x] = creature
        self.grid = new_grid

    def draw(self, screen, cell_size):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    pygame.draw.rect(
                        screen,
                        self.grid[y][x].color,
                        (x * cell_size, y * cell_size, cell_size, cell_size),
                    )
