import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize teh ship and set its starting point."""
        self.screen = ai_game.screen
        self.screen_rec = ai_game.screen.get_rec()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.mdbottom = self.screen_rect.midbottom

    def bnlitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)