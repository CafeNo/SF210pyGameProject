import pygame
import sys
from typing import List
from Bullet import Bullet


class Player(pygame.sprite.Sprite):
    """
    This Class inherit from Sprite utility class.
    that mean it has methods that hooked for calling in sprite Group.

        - update : callable[self, speed] -> None
        - draw : callable[self, surface] -> None
            draw methods has internal call surfacr.blit( `image`, `rect` )

    add this to spite Group then call a hooked method in Group.

    *** Group Hooked should use in life cycle of game for update thing all sprite only (if use in all behave will raise performace issue.)***
    """

    def __init__(self, pos_x: int, pos_y: int,  speed: int, screen: pygame.Surface) -> None:
        super().__init__()
        self.attack_animation = False
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.hp: int = 100
        self.speed = speed
        self.sprites: List[pygame.Surface] = []
        # self.sprites.append(pygame.image.load('attack_1.png'))
        # self.sprites.append(pygame.image.load('attack_2.png'))
        # self.sprites.append(pygame.image.load('attack_3.png'))
        # self.sprites.append(pygame.image.load('attack_4.png'))
        # self.sprites.append(pygame.image.load('attack_5.png'))
        # self.sprites.append(pygame.image.load('attack_6.png'))
        # self.sprites.append(pygame.image.load('attack_7.png'))
        # self.sprites.append(pygame.image.load('attack_8.png'))
        # self.sprites.append(pygame.image.load('attack_9.png'))
        # self.sprites.append(pygame.image.load('attack_10.png'))
        self.current_sprite: int = 0

        self.playerSprite = pygame.image.load('assets/C.png')
        self.playerSprite = pygame. transform.scale(
            self.playerSprite, (64, 64))
        self.playerSprite_rect = self.playerSprite.get_rect()
        self.image = pygame.Surface((64, 74), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.topleft = [pos_x, pos_y]

        # self.rect.size = [self.playerSprite.get_width(), self.playerSprite.get_height()]
        self.hitbox = [0, 10, self.playerSprite.get_size()]

    # def draw(self):
    #     """
    #     Overwrite draw method in Sprite class. cause Of this class use `self.rect` to draw image on screen.
    #     but we want to use `self.rect_with_hpbar` to draw sprite with hpbar. instreat of `self.rect`
    #     then use `self.rect` for colider detection
    #     *** colider detection of sprite class use internal state `self.rect` for detection ***
    #     (if use `self.rect` for draw sprite then it will cause of colider detection issue , it will detect hit on hpbar )

    #     """

    #     self.screen.blit(self.image, self.rect_with_hpbar)

    def moveLeft(self) -> None:

        self.rect.x -= self.speed
        if self.rect.x <= 5:
            self.rect.x = 5

    def moveRight(self) -> None:

        self.rect.x += self.speed

    # this duplicate check for fix glitch of player move. -> this bug causes of frame update not synchronized to state update.
        # print(self.width)
        if self.rect.x >= self.screen_width - self.rect.width - 5:
            self.rect.x = self.screen_width - self.rect.width - 5

    def moveUp(self) -> None:
        self.rect.y -= self.speed
        if self.rect.y <= self.screen_height/2:
            self.rect.y = self.screen_height/2

    def moveDown(self) -> None:
        self.rect.y += self.speed
        if self.rect.y >= self.screen_height - self.rect.height:
            self.rect.y = self.screen_height - self.rect.height

    def drawHpbar(self) -> None:
        pygame.draw.rect(self.image, (255, 0, 0), [
                         0, 0, self.playerSprite.get_width(), 5])
        pygame.draw.rect(self.image, (0, 255, 0), [
                         0, 0, 64 * (self.hp / 100), 5])

    def update(self) -> None:
        self.image = pygame.Surface((64, self.playerSprite.get_height()+10))
        self.image.blit(self.playerSprite, (0, 10))
        pygame.draw.rect(self.image, (0, 255, 0), [
                         0, 10, self.playerSprite_rect.width, self.playerSprite_rect.height], 2)
        self.drawHpbar()

        # self.image = self.sprites[int(self.current_sprite)]

        pass
