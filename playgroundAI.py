#Name: ELijah Raji
#Class:6th hour
#Assinment: playgroundAI


import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 50, 255)

# Set FPS
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Load character sprites
player1_idle = pygame.image.load('player1_idle.png')  # Replace with your own sprite
player2_idle = pygame.image.load('player2_idle.png')  # Replace with your own sprite
player1_attack = pygame.image.load('player1_attack.png')  # Replace with your own sprite
player2_attack = pygame.image.load('player2_attack.png')  # Replace with your own sprite


# Player class
class Player:
    def __init__(self, x, y, color, controls, sprite_idle, sprite_attack):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.color = color
        self.vel = 5
        self.jump_vel = 15
        self.is_jumping = False
        self.jump_count = 10
        self.health = 100
        self.controls = controls
        self.is_attacking = False
        self.attack_range = 60
        self.sprite_idle = sprite_idle
        self.sprite_attack = sprite_attack
        self.direction = "right"

    def move(self, keys):
        if keys[self.controls['left']] and self.x - self.vel > 0:
            self.x -= self.vel
            self.direction = "left"
        if keys[self.controls['right']] and self.x + self.width + self.vel < SCREEN_WIDTH:
            self.x += self.vel
            self.direction = "right"
        if not self.is_jumping:
            if keys[self.controls['up']]:
                self.is_jumping = True
                self.jump_count = 10
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False

    def attack(self):
        self.is_attacking = True

    def draw(self, screen):
        if self.is_attacking:
            if self.direction == "right":
                screen.blit(self.sprite_attack, (self.x + self.width, self.y + self.height // 4))
            else:
                screen.blit(pygame.transform.flip(self.sprite_attack, True, False),
                            (self.x - self.attack_range, self.y + self.height // 4))
        else:
            if self.direction == "right":
                screen.blit(self.sprite_idle, (self.x, self.y))
            else:
                screen.blit(pygame.transform.flip(self.sprite_idle, True, False), (self.x, self.y))

        self.is_attacking = False


# Collision detection function
def collision(player1, player2):
    if (player1.x + player1.width > player2.x and
            player1.x < player2.x + player2.width and
            player1.y + player1.height > player2.y and
            player1.y < player2.y + player2.height):
        return True
    return False


# Game loop
def game_loop():
    # Load the sprites
    player1_idle = pygame.image.load('player1_idle.png')
    player2_idle = pygame.image.load('player2_idle.png')
    player1_attack = pygame.image.load('player1_attack.png')
    player2_attack = pygame.image.load('player2_attack.png')

    player1 = Player(100, SCREEN_HEIGHT - 150, GREEN,
                     {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'attack': pygame.K_f}, player1_idle,
                     player1_attack)
    player2 = Player(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 150, BLUE,
                     {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'attack': pygame.K_RSHIFT},
                     player2_idle, player2_attack)

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Player movements
        player1.move(keys)
        player2.move(keys)

        # Player attacks
        if keys[player1.controls['attack']]:
            player1.attack()
        if keys[player2.controls['attack']]:
            player2.attack()

        # Detect collisions (attack hits)
        if player1.is_attacking and collision(player1, player2):
            player2.health -= 1  # Decrease health for player 2
        if player2.is_attacking and collision(player2, player1):
            player1.health -= 1  # Decrease health for player 1

        # Draw players
        player1.draw(screen)
        player2.draw(screen)

        # Display health bars
        pygame.draw.rect(screen, RED, (20, 20, player1.health * 2, 20))
        pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH - 220, 20, player2.health * 2, 20))

        # Display instructions
        text = font.render(f"Player 1 Health: {player1.health}", True, GREEN)
        screen.blit(text, (20, 50))
        text = font.render(f"Player 2 Health: {player2.health}", True, BLUE)
        screen.blit(text, (SCREEN_WIDTH - 220, 50))

        # Check if a player has lost
        if player1.health <= 0:
            text = font.render("Player 2 Wins!", True, BLUE)
            screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
        elif player2.health <= 0:
            text = font.render("Player 1 Wins!", True, GREEN)
            screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False

        pygame.display.update()
        clock.tick(FPS)


# Run the game
game_loop()

# Quit Pygame
pygame.quit()
