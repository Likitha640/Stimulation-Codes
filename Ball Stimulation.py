/*Python Code for Ball Stimulation */
import pygame
import random

# Initialize the game
pygame.init()

# Set the width and height of the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Simulation")

clock = pygame.time.Clock()

# Ball properties
radius = 20
x = width // 2  # Initial x-position
y = height // 2  # Initial y-position
speed_x = random.randint(-5, 5)  # Initial x-velocity
speed_y = random.randint(-5, 5)  # Initial y-velocity
gravity = 0.5  # Acceleration due to gravity

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position and velocity of the ball
    speed_y += gravity
    x += speed_x
    y += speed_y

    # Check for collision with walls
    if x + radius > width or x - radius < 0:
        speed_x = -speed_x
    if y + radius > height or y - radius < 0:
        speed_y = -speed_y

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()