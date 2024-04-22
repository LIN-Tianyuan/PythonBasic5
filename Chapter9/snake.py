import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définir le titre de la fenêtre
pygame.display.set_caption('Snake')

# Définir la taille de la fenêtre
window_x = 720
window_y = 480

# Initialisation de la fenêtre de jeu
screen = pygame.display.set_mode((window_x, window_y))

# Définir la position par défaut du serpent
snake_position = [100, 50]
# Définir les 4 premiers blocs du corps du serpent
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
# La position des fruits
apple_position = [random.randint(0, window_x), random.randint(0, window_y)]


def show_score(color):
    score_font = pygame.font.SysFont('Arial', 60)
    score_surface = score_font.render("Score: ", True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


while True:
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(apple_position[0], apple_position[1], 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()   # Mise à jour du contenu de l'écran

