import pygame
import cv2
from pygame import mixer
from components.Button import Button

import sys


class lifeAfterDead:

    def __init__(self, loginScreen) -> None:

        # apicture blit at the bottom of the screen line
        # button input x,y in fuction for blitting.

        # load picture and asset
        self.loginScreen = loginScreen
        self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")
        self.success, video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

        # create button
        self.window = pygame.display.set_mode(video_image.shape[1::-1])
        self.clock = pygame.time.Clock()
        self.btn_play = Button(self.window, "./assets/play_menu/pic_play.png",
                               "./assets/play_menu/pic_play_hover.png", 627, 372)
        self.btn_max_score = Button(self.window, "./assets/play_menu/pic_max_score.png",
                                    "./assets/play_menu/pic_max_score_hover.png", 627, 472)
        self.btn_logout = Button(self.window, "./assets/play_menu/pic_logout.png",
                                 "./assets/play_menu/pic_logout_hover.png", 627, 574)

        self.btn_setting = Button(self.window, "./assets/mainmenu/pic_setting.png",
                                  "./assets/mainmenu/pic_setting_hover.png", 930, 27)
        self.logo_game_name = Button(self.window, "./assets/mainmenu/logo_game_name.png",
                                     "./assets/mainmenu/logo_game_name.png", 507, 131)

        self.rect = self.window.get_rect()

        # run this page, by calling run_login_event_loop()
        self.run_login_event_loop()

    def run_login_event_loop(self) -> None:
        while True:

            self.clock.tick(self.fps)

            # get mouse event from each button
            self.mouse_pos = pygame.mouse.get_pos()
            self.btn_play.isHovered(self.mouse_pos)
            self.btn_max_score.isHovered(self.mouse_pos)
            self.btn_logout.isHovered(self.mouse_pos)

            self.btn_setting.isHovered(self.mouse_pos)
            self.logo_game_name.isHovered(self.mouse_pos)

            # do task according to mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.btn_play.checkForInput(self.mouse_pos):
                        print("Onclicked-play")
                        # mixer.music.stop()

                        # mixer.music.pause() # pause bgm

                    if self.btn_max_score.checkForInput(self.mouse_pos):
                        print("Onclicked-max-score")
                    if self.btn_logout.checkForInput(self.mouse_pos):
                        self.loginScreen()
                        print("Onclicked-log-out")
                    if self.btn_setting.checkForInput(self.mouse_pos):
                        print("Onclicked-setting")

            success, video_image = self.video.read()

            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
            else:
                self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")

            # draw button and background video
            self.window.blit(video_surf, (0, 0))
            self.btn_play.draw()
            self.btn_max_score.draw()
            self.btn_logout.draw()

            self.btn_setting.draw()
            self.logo_game_name.draw()

            pygame.display.flip()
