# Importation des modules requis
import pygame
import sys

# Initialiser
pygame.init()

# Configuration de la fenêtre de l'écran d'accueil
screen = pygame.display.set_mode((400, 400))
# Définir le titre de la fenêtre, c'est-à-dire le nom du jeu
pygame.display.set_caption('My first game')
# Introduction des type de polices
f = pygame.font.SysFont('Arial', 60)
# Remplir la couleur de fond de la fenêtre principale
screen.fill((156, 156, 156))
"""
Génère un message texte
Paramètre:
Le contenu du texte
La police est lisse ou non
La police en mode RGB
La couleur de fond de la police en mode RGB
"""
text = f.render("Happy game", True, (255, 218, 185), (255, 0, 0))
# Obtenir les coordonnées de la zone rectangulaire de l'objet affiché
textRect = text.get_rect()
# Définir l'objet d'affichage pour qu'il soit centré
textRect.center = (200, 200)
# Prenez le message texte préparé et dessinez-le sur l'écran d'accueil
screen.blit(text, textRect)
while True:
    # Boucle pour les événements et écoute pour le statut de l'événement
    for event in pygame.event.get():
        # Déterminez si l'utilisateur a cliqué sur le bouton de fermeture "x"
        # et exécutez le segment de code "if"
        if event.type == pygame.QUIT:
            # Désinstaller tous les modules
            pygame.quit()
            # Terminer la procédure et assurer la sortie de celle-ci
            sys.exit()
    pygame.display.flip()   # Mise à jour du contenu de l'écran

