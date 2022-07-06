
import pygame
from player import Player
from Bullet import Bullet
from typing import List, Tuple
import sys
import math
from Enemy import Enemy
import random
from lifeAfterDead import lifeAfterDead
from pygame import mixer
from typing import TYPE_CHECKING
# from loginScreen import LoginScreen
if TYPE_CHECKING:
    from loginScreen import LoginScreen


class GameScreen:

    def __init__(self, loginScreen, playMenu) -> None:

        # Use This case of having multiple screens

        # TODO : close menu BGM
        mixer.Channel(0).pause()
        mixer.Channel(1).unpause()

        self.loginScreen: LoginScreen = loginScreen
        self.playMenu = playMenu
        self.font = pygame.font.Font(
            "./assets/fonts/CrimsonText-Regular.ttf", 24)
        self.screen_size = (1000, 721)
        # center of screen that player can play
        self.gameScreen_size: Tuple[int, int] = (743, 721)
        self.sideScreen_size = (
            math.ceil((self.screen_size[0]-self.gameScreen_size[0])/2)-1, 721)

        self.screen: 'pygame.Surface' = pygame.display.set_mode(
            self.screen_size)
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()

        # game page animation( by looping ) background
        self.bg_width = 1000
        self.bg_height = 4248.8
        self.bg = pygame.image.load('./assets/bg.png')
        self.bg = pygame.transform.scale(
            self.bg, (self.bg_width, self.bg_height))
        self.bg_rect = self.bg.get_rect()
        self.move = True
        self.bg_x: int = 0
        self.bg_y1: int = 0
        self.bg_y2: int = -4248.8
        self.reset()

        # load black tab aside the screen from this.fuction -> drawSideScreen
        self.sideScreen = self.drawSideScreen()
        self.sideScreen_rect = self.sideScreen.get_rect()

        # center of screen that player can play
        self.gameScreenCanvas = self.drawGameScreen()
        self.rect = self.gameScreenCanvas.get_rect()
        self.player = Player(
            self.rect.width/2, self.rect.height-74, 10, self.gameScreenCanvas)

        # seperate team ! player vs enemy !
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.Group()
        self.enemy_group.add(
            Enemy(self.rect.width/2, 0, self.gameScreenCanvas, 100,  "./assets/minion/pic_minion_enemy.png"))
        self.bossSpawn = False
        self.bossIns = Enemy(0, 0, self.gameScreenCanvas,
                             1,  "./assets/characterModel/pic_b1_model.png")
        self.bossIns.kill()

        # Game Internal State for game logic
        self.moveState: List[str] = []
        self.fireState: bool = False
        self.fireDurations: int = 0
        self.score = 0
        self.level = 1

        # game screen display decoration ! score !
        self.score_label = self.font.render(
            "Score:", True, (255, 255, 255))
        self.score_text = self.font.render(
            str(self.score), True, (255, 255, 255))
        self.score_label_rect = self.score_label.get_rect()
        self.score_label_rect.center = (
            self.screen.get_width()-(self.sideScreen_rect.width/2), 50)
        self.score_rect = self.score_text.get_rect()

        # game screen display decoration ! Level !
        self.level_label = self.font.render("Level:", True, (255, 255, 255))
        self.level_label_rect = self.level_label.get_rect()
        self.level_text = self.font.render(
            str(self.level), True, (255, 255, 255))
        self.level_text_rect = self.level_text.get_rect()
        self.level_label_rect.center = (self.sideScreen_rect.width/2, 50)
        self.level_text_rect.center = (self.sideScreen_rect.width/2, 80)

        # self.magicNumberRatio = 1000 - 743 - 128 - 128
        self.enemy_spawn_rate = 0.0095
        self.enemy_spawn_rate_increase = 0.0025
        self.enemy_spawn_rate_increase_rate = 0.0090
        self.killCount = 0
        self.run_game_event_loop()

    def draw(self) -> None:
        """
        This method performs the drawing of the game screen Canvas and inherited call the lifecycle Methods of child instance. (Life cycle -> draw -> update).
        """

        self.gameScreenCanvas = self.drawGameScreen()

        self.player_group.draw(self.gameScreenCanvas)

        self.bullet_group.draw(self.gameScreenCanvas)

        self.enemy_group.draw(self.gameScreenCanvas)
        self.enemy_bullet_group.draw(self.gameScreenCanvas)
        self.boss_group.draw(self.gameScreenCanvas)

        self.screen.blit(self.bg, (self.bg_x, self.bg_y1))
        self.screen.blit(self.bg, (self.bg_x, self.bg_y2))
        self.drawScoreboard()

        self.screen.blit(self.gameScreenCanvas, (self.sideScreen_size[0]+1, 0))

        # inherit draw and update to gameScreenCanvas draw() and update()

    # Player Inherit interface for user interaction to player Instance.

    def drawSideScreen(self):
        s = pygame.Surface(self.sideScreen_size)
        s.set_alpha(100)
        s.fill((0, 0, 0))
        return s

    def drawScoreboard(self):

        # draw level -> decoration display at point(0,0)
        self.sideScreen = self.drawSideScreen()
        self.level_text = self.font.render(
            str(self.level), True, (255, 255, 255))
        self.screen.blit(self.sideScreen, (0, 0))
        self.screen.blit(self.level_label, self.level_label_rect)
        self.screen.blit(self.level_text, self.level_text_rect)

        # draw level -> decoration display at rightside of screen
        self.sideScreen = self.drawSideScreen()
        self.score_text = self.font.render(
            str(self.score), True, (255, 255, 255))
        self.screen.blit(self.sideScreen, (self.rect.width +
                         self.sideScreen_size[0], 0))
        self.screen.blit(self.score_label, self.score_label_rect)
        self.score_rect.center = (
            self.screen.get_width()-(self.sideScreen_rect.width/2), 80)
        self.screen.blit(self.score_text, self.score_rect)

        # self.sideScreen.blit(self.score_text, (self.sideScreen_rect.width/2 - self.sek, 0))

    def run_game_event_loop(self) -> None:
        """
        Use this methods when this seperate screen from another pygame loop. toCreate another gameloop.
        """

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Key Press Event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        self.moveRight()
                    if event.key == pygame.K_UP:
                        self.moveUp()
                    if event.key == pygame.K_DOWN:
                        self.moveDown()
                    if event.key == pygame.K_SPACE:
                        self.fireState = True
                # Key Release Event
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.moveState.remove("left")
                    if event.key == pygame.K_RIGHT:
                        self.moveState.remove("right")
                    if event.key == pygame.K_UP:
                        self.moveState.remove("up")
                    if event.key == pygame.K_DOWN:
                        self.moveState.remove("down")
                    if event.key == pygame.K_SPACE:
                        self.fireState = False

            # Render Frame
            self.screen.fill((0, 0, 0))
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(60)

    def moveRight(self) -> None:
        self.moveState.append("right")

    def moveLeft(self) -> None:
        self.moveState.append("left")

    def moveUp(self) -> None:
        self.moveState.append("up")

    def moveDown(self) -> None:
        self.moveState.append("down")

    def fire(self) -> None:
        """
        player fire the Bullet but creatior of bullet should be the `gameScreen` instance , not `player` instance. Because `gameScreen` instance has Bullet Group that frequently use in game.
        And `gameScreen` instance has information to create `bullet` instance. this fravor following the creator pattern of Grasp priciple.
        """
        # this is for player
        if self.fireState and self.player.alive():
            self.bullet_group.add(
                Bullet(self.player.rect.x+(self.player.rect.width/2)-14, self.player.rect.y, 10, (0, -10), "assets/lazer/pic_model_lazer_ball.png"))
            self.bullet_group.add(
                Bullet(self.player.rect.x+(self.player.rect.width/2)-14, self.player.rect.y, 10, (3, -10), "assets/lazer/pic_model_lazer_ball.png"))
            self.bullet_group.add(
                Bullet(self.player.rect.x+(self.player.rect.width/2)-14, self.player.rect.y-54, 10, (-3, -10), "assets/lazer/pic_model_lazer_ball.png"))

    def update(self) -> None:
        """
        update state of gameScreenCanvas of blit new  thing to surface
        """
        self.bg_update()

        self.playerFire_update()

        self.playerMovements_update()

        self.player_group.update()
        self.bullet_group.update(2.5)
        self.enemy_bullet_group.update()
        self.enemy_group.update()
        self.boss_group.update()
        # for enemy in self.enemy_group:
        #     enemy: Enemy
        self.hit_detection()
        self.enemy_fire()
        self.spawn_enemy()

    def spawn_enemy(self):
        rand_x = random.randint(0, self.rect.width)
        rand_y = random.randint(0, math.ceil(self.rect.height/2))
        if self.bossSpawn and self.level % 3 == 0 and not self.bossIns.alive():
            self.bossSpawn = False
            # mixer.Channel(0).pause()
            # mixer.Channel(1).play(mixer.Sound(
            #     './assets/sound_bgm/FearfulUtopia.mp3'), -1, 5000)
            print("Boss spawn")
            self.bossIns = Enemy(rand_x,  rand_y, self.gameScreenCanvas,
                                 100 * self.level, "./assets/characterModel/pic_b1_model.png")

            self.boss_group.add(self.bossIns
                                )

        if random.random() <= self.enemy_spawn_rate:

            if self.enemy_group.__len__() < math.floor(self.level * 2.5):
                self.enemy_group.add(
                    Enemy(rand_x,  rand_y, self.gameScreenCanvas, 50 * self.level, "./assets/minion/pic_minion_enemy.png"))

    def enemy_fire(self):
        for enemy in self.enemy_group:
            enemy: Enemy
            if enemy.isFire:
                direction = [random.randint(-1, 1), 1]

                self.enemy_bullet_group.add(
                    Bullet(enemy.rect.x+(enemy.rect.width/2)-14, enemy.rect.y+enemy.rect.height, 10, (direction[0]*random.randint(1, 5), direction[1]*5), "assets/lazer/pic_minion_lazer_ball.png"))
                enemy.isFire = False

        boss = self.bossIns

        if boss.isFire and boss.alive():
            print("boss skill")
            direction = [random.uniform(-1.0, 1), 1]
            magicNumber = random.randrange(0, 2)
            if magicNumber == 0:
                for i in range(10):
                    self.enemy_bullet_group.add(
                        Bullet(boss.rect.x+(boss.rect.width/2)-14, boss.rect.y+boss.rect.height, 20, (random.uniform(-1.0, 1)*random.randint(1, 5), direction[1]*5), "assets/lazer/pic_enemy_lazer_ball.png"))
                boss.isFire = False
            else:
                for i in range(10):
                    self.enemy_bullet_group.add(
                        Bullet(boss.rect.x+(boss.rect.width/2)-14, boss.rect.y+boss.rect.height, 50, (random.uniform(-1.0, 1)*random.randint(1, 5), direction[1]*5), "assets/lazer/boss_laser.png"))
                boss.isFire = False

    def hit_detection(self):

        #  this foi is the boss origin
        for boss in self.boss_group:
            mixer.Channel(1).pause()
            mixer.Channel(2).unpause()
            for bullet in self.bullet_group:
                bullet: Bullet
                if pygame.sprite.collide_rect(boss, bullet):
                    boss.hp -= bullet.damage
                    bullet.kill()
                    if boss.hp <= 0 and boss.alive():
                        boss.kill()
                        mixer.Channel(2).pause()
                        mixer.Channel(1).unpause()

        for enemy in self.enemy_group:
            enemy: Enemy
            for bullet in self.bullet_group:
                bullet: Bullet
                if pygame.sprite.collide_rect(enemy, bullet):
                    enemy.hp -= bullet.damage
                    bullet.kill()
                    if enemy.hp <= 0 and enemy.alive():
                        enemy.kill()
                        if not (self.bossSpawn and self.bossIns.alive()):
                            self.killCount += 1
                        oldLevel = self.level
                        self.level = (self.killCount // 6) + 1
                        if self.level > oldLevel:
                            self.bossSpawn = True

                        self.enemy_spawn_rate_increase_rate = (
                            0.01 * self.level)+0.001

        # ! count Score at this line !
                        self.score += 1

                        if random.random() < self.enemy_spawn_rate_increase_rate:
                            self.enemy_spawn_rate += self.enemy_spawn_rate_increase
                            print("Spawn rate increated to ",
                                  self.enemy_spawn_rate)

                        # self.enemy_group.add(
                        #     Enemy(self.rect.width/2, 0, self.gameScreenCanvas, 100))

            if pygame.sprite.collide_rect(enemy, self.player):
                self.player.hp -= enemy.damage
                if self.player.hp <= 0:
                    self.player.kill()
                    # self.game_over()

        for enemy_bullet in self.enemy_bullet_group:
            for player_bullet in self.bullet_group:
                if pygame.sprite.collide_rect(enemy_bullet, player_bullet):
                    enemy_bullet.kill()
                    player_bullet.kill()

            if pygame.sprite.collide_rect(enemy_bullet, self.player):
                self.player.hp -= enemy_bullet.damage
                enemy_bullet.kill()
                if self.player.hp <= 0:
                    self.player.kill()
                    # TODO : open menu BGM
                    mixer.Channel(0).unpause()
                    mixer.Channel(1).pause()
                    mixer.Channel(2).pause()

                    lifeAfterDead(self.loginScreen, self.playMenu)

                    # self.game_over()

    def playerFire_update(self) -> None:
        if self.fireState and self.fireDurations > 6:
            self.fire()
            self.fireDurations = 0
        else:
            if self.fireDurations <= 6:
                self.fireDurations += 2

    def drawGameScreen(self) -> pygame.Surface:
        """
        This methods draw a game screen Surface.
        """
        gameScreenCanvas = pygame.Surface(
            self.gameScreen_size, pygame.SRCALPHA, 32)
        # gameScreenCanvas = gameScreenCanvas.convert()
        gameScreenCanvas.convert_alpha()
        return gameScreenCanvas

    def bg_update(self) -> None:
        """
        This methods update the background of game screen.
        """
        if self.move:
            self.bg_y1 += 2
            self.bg_y2 += 2

            if self.bg_y1 >= self.bg_height:
                self.bg_y1 = -self.bg_height
            if self.bg_y2 >= self.bg_height:
                self.bg_y2 = -self.bg_height

    def playerMovements_update(self) -> None:
        if "left" in self.moveState and "up" in self.moveState:
            self.player.moveLeft()
            self.player.moveUp()
            return None
        if "left" in self.moveState and "down" in self.moveState:
            self.player.moveLeft()
            self.player.moveDown()
            return None
        if "right" in self.moveState and "up" in self.moveState:
            self.player.moveRight()
            self.player.moveUp()
            return None
        if "right" in self.moveState and "down" in self.moveState:
            self.player.moveRight()
            self.player.moveDown()
            return None
        if "right" in self.moveState:
            self.player.moveRight()
            return None
        if "left" in self.moveState:
            self.player.moveLeft()
            return None
        if "up" in self.moveState:
            self.player.moveUp()
            return None
        if "down" in self.moveState:
            self.player.moveDown()
            return None

    def reset(self):
        self.bg_x = 0
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
