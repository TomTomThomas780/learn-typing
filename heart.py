import pygame
 
from pygame.sprite import Sprite
 
class Heart(Sprite):
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/ProgramData/learn_typing/images/heart.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

