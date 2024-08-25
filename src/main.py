import pygame
import sys
from utils.config_loader import get_config
from grid import Grid

# Load configuration
config = get_config("config/config.yaml")

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = config["display"]["width"], config["display"]["height"]
GRID_SIZE = config["simulation"]["grid_size"]
NUM_CREATURES = config["simulation"]["num_creatures"]
CELL_SIZE = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Creature Evolution Simulation")

# Create the grid and populate it with creatures
grid = Grid(GRID_SIZE, GRID_SIZE, NUM_CREATURES)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid
    grid.update()

    # Fill the screen with white
    screen.fill(tuple(config["colors"]["white"]))

    # Draw the grid
    grid.draw(screen, CELL_SIZE)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
