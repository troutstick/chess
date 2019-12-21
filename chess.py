import pygame
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Chess')
running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()