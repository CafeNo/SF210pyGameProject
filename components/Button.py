import pygame


class Button():
    def __init__(self, screen: pygame.Surface, basePicture: str, hoverPicture: str, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.basePicture = pygame.image.load(basePicture)
        self.hoverPicture = pygame.image.load(hoverPicture)

        self.image = pygame.Surface(
            (self.basePicture.get_rect().width, self.basePicture.get_rect().height))
        self.rect = self.image.get_rect()

        self.rect.topleft = (self.x, self.y)

    def draw(self):

        self.screen.blit(self.image, self.rect)

    # def update(self):

    def isHovered(self, mouse_position):
        
        self.image = pygame.Surface(
            (self.basePicture.get_rect().width, self.basePicture.get_rect().height), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            self.image.blit(self.hoverPicture, (0, 0))
        else:
            self.image.blit(self.basePicture, (0, 0))

    def checkForInput(self, mouse_position):
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
