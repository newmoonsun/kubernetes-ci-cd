import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Airplane Shooter")

# Load airplane and bullet images
airplane_img = pygame.image.load(os.path.join("airplane.png"))
bullet_img = pygame.image.load(os.path.join("bullet.png"))

# Airplane class
class Airplane:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(airplane_img, (self.x, self.y))

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(bullet_img, (self.x, self.y))

# Main game loop
airplane = Airplane(WIDTH // 2 - airplane_img.get_width() // 2, HEIGHT - airplane_img.get_height() - 10)
bullets = []
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(airplane.x + airplane_img.get_width() // 2 - bullet_img.get_width() // 2, airplane.y)
                bullets.append(bullet)

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and airplane.x > 0:
        airplane.x -= 5
    if keys[pygame.K_RIGHT] and airplane.x < WIDTH - airplane_img.get_width():
        airplane.x += 5

    # Update bullets
    for bullet in bullets:
        bullet.move()
        if bullet.y < -bullet_img.get_height():
            bullets.remove(bullet)

    # Draw everything
    screen.fill((0, 0, 0))
    airplane.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()
