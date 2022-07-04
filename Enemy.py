import pygame
import sys
from typing import List
from Bullet import Bullet
import random

class Enemy(pygame.sprite.Sprite):
    """
    This Class inherit from Sprite utility class.
    that mean it has methods that hooked for calling in sprite Group.

        - update : callable[self, speed] -> None
        - draw : callable[self, surface] -> None
            draw methods has internal call surfacr.blit( `image`, `rect` )

    add this to spite Group then call a hooked method in Group.

    *** Group Hooked should use in life cycle of game for update thing all sprite only (if use in all behave will raise performace issue.)***
    """

    def __init__(self, pos_x: int, pos_y: int, screen: pygame.Surface,hp:int) -> None:
        super().__init__()
       
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sprite = pygame.image.load('assets/minion/pic_minion_enemy.png')
        self.sprite = pygame. transform. scale(self.sprite, (self.sprite.get_width(), self.sprite.get_height()))
        self.image = pygame.Surface((64,74))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.pace_size   = 3             # How big each step is
        self.pace_count_x  = 0                # distance moved
        self.pace_count_y  = 0 
        self.direction   = [-1,1]              # Start moving left (-x)
        self.turn_after  = 25       # distance limit
        self.speed       = 5            # Milliseconds per pace
        self.pace_time   = 0                # time of last step
        self.maxHp = hp
        self.hp = hp
        
        self.damage = 10
        self.isFire = True
        self.fireCount = 0
        pygame.draw.rect(self.image, (0, 0, 255), [0, 0, 64, 64], 2)


    def update(self):
        time_now = pygame.time.get_ticks()               # what time is it
        self.image = pygame.Surface((64, self.sprite.get_height()+10))
        self.image.blit(self.sprite, (0, 10))

        # debug frame
        # pygame.draw.rect(self.image, (0, 0, 255), [
        #                  0, 10, self.rect.width, self.rect.height-10], 2)
        self.drawHpbar()
        if ( time_now > self.pace_time + self.speed ):   # is it time to move again
            self.pace_time = time_now

            # Walk pace in the current direction
            self.pace_count_x += 1
            self.pace_count_y += 1
            self.rect.x     += self.direction[0] * self.pace_size     # Move some pixels
            self.rect.y     += self.direction[1] * self.pace_size     # Move some pixels

            # We need to turn around if walked enough paces in the same direction
            if ( self.pace_count_x >= self.turn_after  and self.pace_count_y >= self.turn_after):
                # Turn around!
                self.direction[0] = random.randint(-1,1)         # reverses the pixel distance
                self.direction[1] = random.randint(-1,1)         # reverses the pixel distance
                self.pace_count_x = 0            # reset the pace count
                self.pace_count_y = 0

            # We also should change direction if we hit the screen edge
            if ( self.rect.x <= 5 ):
                # self.direction  = 1             # turn right
                self.direction[0] = 1         # reverses the pixel distance
                self.direction[1] = random.randint(-1,1)      

                self.pace_count_x = 0
                
            elif ( self.rect.x >= self.screen_rect.width - self.rect.width ):
                self.direction[0]  = -1
                self.direction[1]  = random.randint(-1,1)
                self.pace_count_x = 0

            if self.rect.y <= 5:
                self.direction[0] = random.randint(-1,1)     
                self.direction[1] = 1

                self.pace_count_y = 0

            elif ( self.rect.y >= self.screen_rect.height/2 - self.rect.height ):
                self.direction[0] = random.randint(-1,1)     
                self.direction[1] = -1

                self.pace_count_y = 0
            

            if self.hp <= 0 :
                self.kill()
        if random.randint(0,100) <= 50:
            self.fireCount +=1
            if self.fireCount >= 20:
                self.isFire = True
                self.fireCount = 0
            
            
        
    def drawHpbar(self) -> None:
        pygame.draw.rect(self.image, (255, 0, 0), [
                         0, 0, self.sprite.get_width(), 5])
        pygame.draw.rect(self.image, (0, 255, 0), [
                         0, 0, 64 * (self.hp / self.maxHp), 5])

   


    