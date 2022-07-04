
import pygame
import cv2
from pygame import mixer
from components.Button import Button
import sys
from StateManager import StateManager
from playMenu import PlayMenu
class Register:
    
    def __init__(self,loginScreen) -> None:  

        # apicture blit at the bottom of the screen line
        # button input x,y in fuction for blitting.
        self.store = StateManager()
        #load picture and asset
        self.loginScreen = loginScreen
        self.video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")
        self.success, video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.overlay = pygame.image.load("./assets/login_entry/shadow_overlay.png")
        self.register_screen = pygame.image.load("./assets/pic_bg_register.png")
        self.bg_success = pygame.image.load("./assets/pic_bg_success.png")
        self.isClickedRegist = False

        # create button
        self.window = pygame.display.set_mode(video_image.shape[1::-1])
        self.clock = pygame.time.Clock()
        self.btn_login = Button(self.window,"./assets/mainmenu/pic_login.png", "./assets/mainmenu/pic_login.png", 627, 399)
        self.btn_register = Button(self.window, "./assets/mainmenu/pic_register.png","./assets/mainmenu/pic_register.png", 627, 539)
        self.btn_setting = Button(self.window, "./assets/mainmenu/pic_setting.png",
                            "./assets/mainmenu/pic_setting_hover.png", 930, 27)
        self.logo_game_name = Button(self.window, "./assets/mainmenu/logo_game_name.png",
                                "./assets/mainmenu/logo_game_name.png", 507, 131)
        self.btn_x = Button(self.window, "./assets/pic_x.png",
                                "./assets/pic_x_hover.png", 851, 113)
        # self.btn_regist = Button(self.window, "./assets/pic_regist.png",
        #                         "./assets/pic_regist_hover.png", 466, 572)
        self.btn_mini_play = Button(self.window, "./assets/pic_mini_play.png",
                                "./assets/pic_mini_play_hover.png", 468, 558)

        # character Icon button a
        self.btn_a1 = Button(self.window, "./assets/characterProfile/pic_a1.png",
                                "./assets/characterProfile/pic_a1_hover.png", 216, 308)
        self.btn_a2 = Button(self.window, "./assets/characterProfile/pic_a2.png",
                                "./assets/characterProfile/pic_a2_hover.png", 372, 308)
        self.btn_a3 = Button(self.window, "./assets/characterProfile/pic_a3.png",
                                "./assets/characterProfile/pic_a3_hover.png", 528, 308)
        self.btn_a4 = Button(self.window, "./assets/characterProfile/pic_a4.png",
                                "./assets/characterProfile/pic_a4_hover.png", 684, 308)
        
        # character Icon button b
        self.btn_b1 = Button(self.window, "./assets/characterProfile/pic_b1.png",
                                "./assets/characterProfile/pic_b1_hover.png", 216, 433)
        self.btn_b2 = Button(self.window, "./assets/characterProfile/pic_b2.png",
                                "./assets/characterProfile/pic_b2_hover.png", 372, 433)
        self.btn_b3 = Button(self.window, "./assets/characterProfile/pic_b3.png",
                                "./assets/characterProfile/pic_b3_hover.png", 528, 433)
        self.btn_b4 = Button(self.window, "./assets/characterProfile/pic_b4.png",
                                "./assets/characterProfile/pic_b4_hover.png", 684, 433)


        self.rect = self.window.get_rect()
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
            self.btn_x.isHovered(self.mouse_pos)
            # self.btn_regist.isHovered(self.mouse_pos)
            self.btn_mini_play.isHovered(self.mouse_pos)

            # character a1
            self.btn_a1.isHovered(self.mouse_pos)
            self.btn_a2.isHovered(self.mouse_pos)
            self.btn_a3.isHovered(self.mouse_pos)
            self.btn_a4.isHovered(self.mouse_pos)

            # character b1
            self.btn_b1.isHovered(self.mouse_pos)
            self.btn_b2.isHovered(self.mouse_pos)
            self.btn_b3.isHovered(self.mouse_pos)
            self.btn_b4.isHovered(self.mouse_pos)
                

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
                    if self.btn_x.checkForInput(self.mouse_pos):
                        self.loginScreen()          
                        print("btn_x")
                    # if self.btn_regist.checkForInput(self.mouse_pos):
                    #     print("btn_regist")
                    #     self.isClickedRegist = True
                    if self.btn_mini_play.checkForInput(self.mouse_pos):
                        print("Onclicked-login")
                        PlayMenu(self.loginScreen)

                     


                    # character set Event
                    if self.btn_a1.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_a1_model.png")
                        self.isClickedRegist = True
                        
                    if self.btn_a2.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_a2_model.png")
                        self.isClickedRegist = True
                    if self.btn_a3.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_a3_model.png")
                        self.isClickedRegist = True
                    if self.btn_a4.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_a4_model.png")
                        self.isClickedRegist = True

                    # character set Event
                    if self.btn_b1.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_b1_model.png")
                        self.isClickedRegist = True

                    if self.btn_b2.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_b2_model.png")
                        self.isClickedRegist = True

                    if self.btn_b3.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_b3_model.png")
                        self.isClickedRegist = True

                    if self.btn_b4.checkForInput(self.mouse_pos):
                        self.store.__setitem__("playerModel","./assets/characterModel/pic_b4_model.png")
                        self.isClickedRegist = True




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
            self.window.blit(self.register_screen, (98, 91))
            self.btn_x.draw()

            # draw character a
            self.btn_a1.draw()
            self.btn_a2.draw()
            self.btn_a3.draw()
            self.btn_a4.draw()

            # draw character b
            self.btn_b1.draw()
            self.btn_b2.draw()
            self.btn_b3.draw()
            self.btn_b4.draw()

            if self.isClickedRegist:
                self.window.blit(self.bg_success, (98, 91))
                self.btn_x.draw()
                self.btn_mini_play.draw()


    
           

            pygame.display.flip()



        