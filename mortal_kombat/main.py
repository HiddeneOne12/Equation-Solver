import pygame
import sys
from threading import Timer
# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fighting Game - Hit boxes and Health Bars")

# Colors
WHITE = (255, 255, 255)
DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Character attributes
CHAR_WIDTH, CHAR_HEIGHT = 50, 100
HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT = 200, 30

# Character 1 properties
char1_pos = [100, 400]  # Initial position
char1_health = 100

# Character 2 properties
char2_pos = [600, 400]  # Initial position
char2_health = 100
max_health = 100
current_health = max_health
max_health2 = 100
current_health2 = max_health2
is_jumped = False
# Game loop
clock = pygame.time.Clock()
FPS = 60

game_background_image = pygame.image.load("mortal_kombat/images/background/war.jpg")
game_background_image = pygame.transform.scale(game_background_image,(WIDTH,HEIGHT)).convert_alpha()

def move_character_down():
    global is_jumped
    if is_jumped:
        char2_pos[1] = 400 
        char1_pos[1] = 400 
        is_jumped = False

def draw_health_bar(screen, x, y, health, max_health):
    # Calculate health ratio
    health_ratio = health / max_health  

    # Draw the background bar (black border)
    pygame.draw.rect(screen, BLACK, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT), border_radius=8)

    # Define the colors for gradient (Green -> Yellow -> Red)
    if health_ratio > 0.5:
        health_color = GREEN
    elif 0.2 < health_ratio <= 0.5:
        health_color = YELLOW
    else:
        health_color = RED

    # Draw the filled bar (health bar)
    filled_width = int(HEALTH_BAR_WIDTH * health_ratio)
    inner_bar = pygame.Rect(x + 5, y + 5, filled_width - 10, HEALTH_BAR_HEIGHT - 10)
    pygame.draw.rect(screen, health_color, inner_bar, border_radius=5)

    # Draw the health text
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"HP: {int(health)} / {max_health}", True, WHITE)
    screen.blit(text, (x + (HEALTH_BAR_WIDTH // 2) - text.get_width() // 2, y + (HEALTH_BAR_HEIGHT // 2) - text.get_height() // 2))

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(WHITE)
    screen.blit(game_background_image,(0,0))

    # Create hitboxes for each character
    char1_hitbox = pygame.Rect(char1_pos[0], char1_pos[1], CHAR_WIDTH, CHAR_HEIGHT)
    shay = pygame.image.load("mortal_kombat/images/sprites/shay.png")
    shay = pygame.transform.scale(shay,(200,200)).convert_alpha()
    char2_hitbox = pygame.Rect(char2_pos[0], char2_pos[1], CHAR_WIDTH, CHAR_HEIGHT)

    # Draw characters (representing hit boxes)
    pygame.draw.rect(screen, RED, char1_hitbox)
    pygame.draw.rect(screen, GREEN, char2_hitbox)
    screen.blit(shay,(char2_pos[0], 350,))
    # Collision detection
    if char1_hitbox.colliderect(char2_hitbox):
            current_health -= 10  
            if current_health < 0:
                current_health = 0  # Prevent health from going below zero
        # Decrease health if a collision is detected
            else:
                current_health2 -= 10  # Reduce health when space is pressed
                if current_health2 < 0:
                 current_health2 = 0  # Prevent health from going below zero
                

    # Draw health bars
    draw_health_bar(screen, 50, 50, current_health, max_health)
    draw_health_bar(screen, 550, 50, current_health2, max_health2)
  

    # Key handling for movement (optional)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        char1_pos[0] -= 5  # Move left
    if keys[pygame.K_d]:
        char1_pos[0] += 5  # Move right
    if keys[pygame.K_UP]:
        char1_pos[1] -= 10  # Move up
        is_jumped = True
        Timer(0.2, move_character_down).start()    
    if keys[pygame.K_LEFT]:
        char2_pos[0] -= 5  # Move left
    if keys[pygame.K_RIGHT]:
        char2_pos[0] += 5  # Move right
    if keys[pygame.K_SPACE]:
        char2_pos[1] -= 10  # Move up
        is_jumped = True
        Timer(0.2, move_character_down).start()
        
    

    # Update the screen
    pygame.display.flip()
    clock.tick(FPS)

