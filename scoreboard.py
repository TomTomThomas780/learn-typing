import pygame.font
from pygame.sprite import Group
 
from heart import Heart

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.prep_hearts()

    def prep_hearts(self):
        """Show how many hearts are left."""
        self.hearts = Group()
        for heart_number in range(self.ai_game.health):
            heart = Heart(self.ai_game)
            heart.rect.x = 10 + heart_number * heart.rect.width
            heart.rect.y = 10
            self.hearts.add(heart)

    def show_score(self):
        self.hearts.draw(self.screen)

