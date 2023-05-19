import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the background image
background_image_path = "download.jpeg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Set the initial position and velocity of the dot
dot_size = 10
dot_speed = 5
dot_x = 0
dot_y = screen_height // 2
dot_direction = 1  # 1 for right, -1 for left

# Load the sound effect
sound_effect_path = "mixkit-retro-game-notification-212.wav"
sound_effect = pygame.mixer.Sound(sound_effect_path)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the dot
    dot_x += dot_speed * dot_direction

    # Check if the dot has hit the right or left edge of the screen
    if dot_x >= screen_width or dot_x <= 0:
        sound_effect.play()
        dot_direction *= -1  # Reverse the direction when hitting the wall

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the dot
    pygame.draw.circle(screen, (255, 255, 255), (dot_x, dot_y), dot_size)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the application
pygame.quit()

