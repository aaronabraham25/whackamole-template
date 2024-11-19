import pygame
import random

# Initialize Pygame.
pygame.init()

# Screen dimensions and grid setup.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 512
GRID_SIZE = 32

# Colors on the screen.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Load mole image and scale it.
mole_image = pygame.image.load('mole.png')  # Replace 'mole.png' with your image file name
mole_image = pygame.transform.scale(mole_image, (GRID_SIZE, GRID_SIZE))

# Initial mole position.
mole_x, mole_y = 0, 0

# Clock for controlling the frame rate.
clock = pygame.time.Clock()

# Score tracking.
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mole was clicked or not
            mouse_x, mouse_y = event.pos
            if (mole_x <= mouse_x < mole_x + GRID_SIZE and
                    mole_y <= mouse_y < mole_y + GRID_SIZE):
                score += 1
                # Move mole to a new random position
                mole_x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
                mole_y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)

    # Clear the whole screen
    screen.fill(WHITE)

    # Draw the full grid
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

    # Draw/put in the mole.
    screen.blit(mole_image, (mole_x, mole_y))

    # Draw the score.
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display of it
    pygame.display.flip()

    # Control the frame rate of it
    clock.tick(60)

pygame.quit()
