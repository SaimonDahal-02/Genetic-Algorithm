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

generation_duration = 300  # Number of frames per generation
# Create the grid and populate it with creatures
grid = Grid(
    GRID_SIZE, GRID_SIZE, NUM_CREATURES, steps_per_generation=generation_duration
)

# Set up font for displaying generation
font = pygame.font.Font(None, 36)

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

    # Display current generation
    generation_text = font.render(
        f"Generation: {grid.generation}", True, (0, 0, 0))
    screen.blit(generation_text, (10, 10))

    if grid.generation > 0:
        survival_text = font.render(
            f"Previous Gen Survival:{grid.survival_rate:.2f}%", True, (0, 0, 0)
        )
        screen.blit(survival_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
