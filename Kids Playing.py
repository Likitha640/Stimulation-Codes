import pygame
import random

# Initialize Pygame
pygame.init()

# Define the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kids Playing in the Garden")

# Load images
kid_image = pygame.image.load("kid.png")
background_image = pygame.image.load("garden.jpg")

# Get the size of the kid image
kid_width, kid_height = kid_image.get_rect().size

# Set the initial position of the kid
kid_x = random.randint(0, screen_width - kid_width)
kid_y = random.randint(0, screen_height - kid_height)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the kid randomly
    kid_x += random.randint(-5, 5)
    kid_y += random.randint(-5, 5)

    # Make sure the kid stays within the screen boundaries
    if kid_x < 0:
        kid_x = 0
    elif kid_x > screen_width - kid_width:
        kid_x = screen_width - kid_width
    if kid_y < 0:
        kid_y = 0
    elif kid_y > screen_height - kid_height:
        kid_y = screen_height - kid_height

    # Draw the background image and kid image on the screen
    screen.blit(background_image, (0, 0))
    screen.blit(kid_image, (kid_x, kid_y))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()