#Name: ELijah Raji
#Class:6th hour
#Assinment: playgroundAI

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini Call of Duty 2D')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Font for score
font = pygame.font.SysFont("Arial", 30)

# Game loop flag
running = True
score = 0

def create_enemy():
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = -enemy_height
    return [enemy_x, enemy_y]

# Main game loop
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        # Shoot a bullet
        bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Update bullet positions
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Create new enemies randomly
    if random.random() < 0.02:
        enemies.append(create_enemy())

    # Update enemy positions and check for collisions
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
        if player_x < enemy[0] + enemy_width and player_x + player_width > enemy[0] and player_y < enemy[1] + enemy_height and player_y + player_height > enemy[1]:
            # Collision with player
            running = False
        for bullet in bullets[:]:
            if enemy[0] < bullet[0] + bullet_width and enemy[0] + enemy_width > bullet[0] and enemy[1] < bullet[1] + bullet_height and enemy[1] + enemy_height > bullet[1]:
                # Bullet hits enemy
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1

    # Draw the player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
