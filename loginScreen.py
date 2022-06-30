import pygame
import cv2
from pygame import mixer
from components.Button import Button
from Gamescreen import GameScreen
import sys
from login_entry import LoginEntry

# this page composed of 3 classed. < LoginScreen , login_entry, play_menu >

class LoginScreen:
    
    def __init__(self) -> None:  

        self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")
        self.success, video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

        # setting menu load picture assets to use with blit_setting()
        self.overlay = pygame.image.load("./assets/login_entry/shadow_overlay.png")


        # fuction chec btn is hovering, if yes then btn will change to hover picture
        self.window = pygame.display.set_mode(video_image.shape[1::-1])
        self.clock = pygame.time.Clock()
        self.btn_login = Button(self.window,"./assets/mainmenu/pic_login.png", "./assets/mainmenu/pic_login_hover.png", 627, 399)
        self.btn_register = Button(self.window, "./assets/mainmenu/pic_register.png",
                            "./assets/mainmenu/pic_register_hover.png", 627, 539)
        self.btn_setting = Button(self.window, "./assets/mainmenu/pic_setting.png",
                            "./assets/mainmenu/pic_setting_hover.png", 930, 27)
        self.logo_game_name = Button(self.window, "./assets/mainmenu/logo_game_name.png",
                                "./assets/mainmenu/logo_game_name.png", 507, 131)


        self.run_login_event_loop()
    def run_login_event_loop(self) -> None:
        while True:
            self.clock.tick(self.fps)

            # fuction chec btn is hovering, if yes then btn will change to hover picture
            self.mouse_pos = pygame.mouse.get_pos()
            self.btn_login.isHovered(self.mouse_pos)
            self.btn_register.isHovered(self.mouse_pos)
            self.btn_setting.isHovered(self.mouse_pos)
            self.logo_game_name.isHovered(self.mouse_pos)

            # get mouse event from each button press
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.btn_login.checkForInput(self.mouse_pos):
                        LoginEntry(LoginScreen)
                        print("Onclicked-login")
                        # mixer.music.pause() # pause bgm
                    if self.btn_register.checkForInput(self.mouse_pos):
                        # gameScreen = GameScreen()
                        print("Onclicked-register")
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.btn_setting.checkForInput(self.mouse_pos):
                            # TODO: Blit menu.
                            print("Onclicked-setting")

            success, video_image = self.video.read()

            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
            else:
                video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")

            self.window.blit(video_surf, (0, 0))
            self.btn_login.draw()
            self.btn_register.draw()
            self.btn_setting.draw()
            self.logo_game_name.draw()

            

            pygame.display.flip()
