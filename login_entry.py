
import pygame
import cv2
from pygame import mixer
from components.Button import Button
from Gamescreen import GameScreen
import sys
from playMenu import PlayMenu
class LoginEntry:
    
    def __init__(self,loginScreen) -> None:  

        # apicture blit at the bottom of the screen line
        # button input x,y in fuction for blitting.

        #load picture and asset
        self.loginScreen = loginScreen
        self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")
        self.success, video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.overlay = pygame.image.load("./assets/login_entry/shadow_overlay.png")
        self.entry_screen = pygame.image.load("./assets/login_entry/entry_screen.png")
        self.line= pygame.image.load("./assets/login_entry/pic_line.png")
        self.name_label= pygame.image.load("./assets/login_entry/pic_name_label.png")
        

        # load background music
        # mixer.init()
        # mixer.music.load('./assets/mainmenu/bgm.mp3')
        # mixer.music.play(-1,fade_ms=5000) # edit music, fade intro

        # create button
        self.window = pygame.display.set_mode(video_image.shape[1::-1])
        self.clock = pygame.time.Clock()
        self.btn_login = Button(self.window,"./assets/mainmenu/pic_login.png", "./assets/mainmenu/pic_login.png", 627, 399)
        self.btn_register = Button(self.window, "./assets/mainmenu/pic_register.png","./assets/mainmenu/pic_register.png", 627, 539)
        self.btn_setting = Button(self.window, "./assets/mainmenu/pic_setting.png",
                            "./assets/mainmenu/pic_setting_hover.png", 930, 27)
        self.logo_game_name = Button(self.window, "./assets/mainmenu/logo_game_name.png",
                                "./assets/mainmenu/logo_game_name.png", 507, 131)
        self.btn_ok = Button(self.window, "./assets/login_entry/pic_ok.png",
                                "./assets/login_entry/pic_ok_hover.png", 390.5, 444.5)
        self.rect = self.window.get_rect()
        self.btn_cancle = Button(self.window, "./assets/login_entry/pic_cancle.png",
                                "./assets/login_entry/pic_cancle_hover.png", 547.5, 443)
        self.rect = self.window.get_rect()

        # run this page, by calling run_login_event_loop()
        self.run_login_event_loop()

    def run_login_event_loop(self) -> None:
        while True:

            self.clock.tick(self.fps)

            # get mouse event from each button
            self.mouse_pos = pygame.mouse.get_pos()
            self.btn_login.isHovered(self.mouse_pos)
            self.btn_register.isHovered(self.mouse_pos)
            self.btn_setting.isHovered(self.mouse_pos)
            self.logo_game_name.isHovered(self.mouse_pos)
            self.btn_ok.isHovered(self.mouse_pos)
            self.btn_cancle.isHovered(self.mouse_pos)

            # do task according to mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.btn_login.checkForInput(self.mouse_pos):
                        print("Onclicked-login")
                        #mixer.music.pause() # pause bgm
                        
                    if self.btn_register.checkForInput(self.mouse_pos):
                        print("Onclicked-register")
                    if self.btn_setting.checkForInput(self.mouse_pos):
                        print("Onclicked-setting")
                    if self.btn_ok.checkForInput(self.mouse_pos):
                        PlayMenu(self.loginScreen)
                        print("btn_ok")
                    if self.btn_cancle.checkForInput(self.mouse_pos):
                        self.loginScreen()                
                        print("btn_cancle")

            success, video_image = self.video.read()

            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
            else:
                self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")

            # draw button and background video
            self.window.blit(video_surf, (0, 0))
            self.btn_login.draw()
            self.btn_register.draw()
            self.btn_setting.draw()
            self.logo_game_name.draw()

            self.window.blit(self.overlay, (0, 0))
            self.window.blit(self.entry_screen, (223, 207))
            self.window.blit(self.line, (500, 450))
            self.btn_ok.draw()
            self.btn_cancle.draw()
            self.window.blit(self.name_label, (285, 333))


            pygame.display.flip()



        