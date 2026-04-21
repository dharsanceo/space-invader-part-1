import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Space Game")
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
player = pygame.Rect(300, 200, 30, 30)
enemies = []
for i in range(7):
    x = random.randint(0, 570)
    y = random.randint(0, 370)
    enemies.append(pygame.Rect(x, y, 30, 30))
score = 0
font = pygame.font.SysFont(None, 30)
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    pygame.draw.rect(screen, blue, player)
    for enemy in enemies:
        pygame.draw.rect(screen, red, enemy)
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 570)
            enemy.y = random.randint(0, 370)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
pygame.quit()