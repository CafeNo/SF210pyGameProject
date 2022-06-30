import pygame
import sys
from typing import List, Tuple


class Bullet(pygame.sprite.Sprite):
    """
    This Class inherit from Sprite utility class.
    that mean it has methods that hooked for calling in sprite Group.

        - update : callable[self, speed] -> None
        - draw : callable[self, surface] -> None
            draw methods has internal call surfacr.blit( `image`, `rect` )

    add this to spite Group then call a hooked method in Group.

    *** Group Hooked should use in life cycle of game for update thing all sprite only (if use in all behave will raise performace issue.)***
    """

    def __init__(self, pos_x: int, pos_y: int, damage: int, vec: Tuple[int, int], image: str) -> None:
        super().__init__()

        self.image = pygame.image.load(image)
        # self.image = pygame. transform. scale(self.image, (64, 64))

        self.attack_animation = False
        self.vec = vec
        self.damage = damage
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        pygame.draw.rect(self.image, (255, 0, 0), [
                         0, 0, self.rect.width, self.rect.height], 2)

    def update(self, speed=1) -> None:
        self.rect.x += self.vec[0]*speed
        self.rect.y += self.vec[1]*speed
        if self.rect.y < -60:
            self.kill()
            # print("Kill Sprite")
        # self.image = self.sprites[int(self.current_sprite)]
