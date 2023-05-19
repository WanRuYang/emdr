import pygame
import os
import glob

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the initial position and velocity of the dot
dot_size = 10
dot_speed = 5
dot_x = 0
dot_y = screen_height // 2
dot_direction = 1  # 1 for right, -1 for left

# Set the default background image and sound effect
default_background_image_path = "download.jpeg"
default_background_image = pygame.image.load(default_background_image_path)
default_background_image = pygame.transform.scale(default_background_image, (screen_width, screen_height))

default_sound_effect_path = "mixkit-retro-game-notification-212.wav"
default_sound_effect = pygame.mixer.Sound(default_sound_effect_path)

# Fetch available soundtracks and images using glob
soundtrack_directory = "."
image_directory = "."

available_soundtracks = glob.glob(os.path.join(soundtrack_directory, "*.wav"))
available_images = glob.glob(os.path.join(image_directory, "*.jpeg"))

# Initialize the selected soundtrack and image
selected_soundtrack = default_sound_effect
selected_image = default_background_image

# UI elements
font = pygame.font.Font(None, 30)

# Speed slider
speed_label = font.render("Speed", True, (255, 255, 255))
speed_rect = speed_label.get_rect(topleft=(10, 10))
speed_slider = pygame.Rect(150, 15, 200, 10)
speed_value = dot_speed

# Volume slider
volume_label = font.render("Volume", True, (255, 255, 255))
volume_rect = volume_label.get_rect(topleft=(10, 40))
volume_slider = pygame.Rect(150, 45, 200, 10)
volume_value = 1.0

# Soundtrack dropdown menu
soundtrack_label = font.render("Soundtrack", True, (255, 255, 255))
soundtrack_rect = soundtrack_label.get_rect(topleft=(10, 70))
soundtrack_dropdown = pygame.Rect(150, 75, 200, 30)
soundtrack_selected = 0

# Image dropdown menu
image_label = font.render("Image", True, (255, 255, 255))
image_rect = image_label.get_rect(topleft=(10, 110))
image_dropdown = pygame.Rect(150, 115, 200, 30)
image_selected = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for UI interaction
        if event.type == pygame.MOUSEBUTTONDOWN:
            if speed_slider.collidepoint(event.pos):
                speed_value = (event.pos[0] - speed_slider.x) / speed_slider.width * 10
                dot_speed = int(speed_value)

            if volume_slider.collidepoint(event.pos):
                volume_value = (event.pos[0] - volume_slider.x) / volume_slider.width
                selected_soundtrack.set_volume(volume_value)

            if soundtrack_dropdown.collidepoint(event.pos):
                soundtrack_selected = (event.pos[1] - soundtrack_dropdown.y) // 30
                selected_soundtrack = pygame.mixer.Sound(available_soundtracks[soundtrack_selected])

            if image_dropdown.collidepoint(event.pos):
                image_selected = (event.pos[1] - image_dropdown.y) // 30
                selected_image = pygame.image.load(available_images[image_selected])
                selected_image = pygame.transform.scale(selected_image, (screen_width, screen_height))

    # Move the dot
    dot_x += dot_speed * dot_direction

    # Check if the dot has hit the right or left edge of the screen
    if dot_x >= screen_width or dot_x <= 0:
        selected_soundtrack.play()
        dot_direction *= -1  # Reverse the direction when hitting the wall

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(selected_image, (0, 0))

    # Draw the dot
    pygame.draw.circle(screen, (255, 255, 255), (dot_x, dot_y), dot_size)

    # Draw UI elements
    pygame.draw.rect(screen, (255, 255, 255), speed_slider)
    pygame.draw.rect(screen, (255, 255, 255), volume_slider)
    pygame.draw.rect(screen, (255, 255, 255), soundtrack_dropdown)
    pygame.draw.rect(screen, (255, 255, 255), image_dropdown)

    screen.blit(speed_label, speed_rect)
    screen.blit(volume_label, volume_rect)
    screen.blit(soundtrack_label, soundtrack_rect)
    screen.blit(image_label, image_rect)

    pygame.draw.rect(screen, (255, 255, 255), (speed_slider.x + int(speed_value * speed_slider.width / 10) - 2, speed_slider.y - 5, 4, 20))
    pygame.draw.rect(screen, (255, 255, 255), (volume_slider.x + int(volume_value * volume_slider.width) - 2, volume_slider.y - 5, 4, 20))
    pygame.draw.rect(screen, (255, 255, 255), soundtrack_dropdown, 2)
    pygame.draw.rect(screen, (255, 255, 255), image_dropdown, 2)

    speed_value_label = font.render(str(int(speed_value)), True, (255, 255, 255))
    speed_value_rect = speed_value_label.get_rect(topright=(350, 10))
    screen.blit(speed_value_label, speed_value_rect)

    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the application
pygame.quit()

