import pygame
import cv2
from pygame import mixer
from components.Button import Button
from Gamescreen import GameScreen


logo = pygame.image.load('./assets/logo.png')
pygame.display.set_icon(logo)

video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

mixer.init()
mixer.music.load('./assets/mainmenu/bgm.mp3')
mixer.music.play(-1,fade_ms=5000)

window = pygame.display.set_mode(video_image.shape[1::-1])
clock = pygame.time.Clock()
btn_login = Button(window,"./assets/mainmenu/pic_login.png", "./assets/mainmenu/pic_login_hover.png", 627, 381)
btn_register = Button(window, "./assets/mainmenu/pic_register.png",
                      "./assets/mainmenu/pic_register_hover.png", 627, 514)
btn_setting = Button(window, "./assets/mainmenu/pic_setting.png",
                     "./assets/mainmenu/pic_setting_hover.png", 930, 27)
logo_game_name = Button(window, "./assets/mainmenu/logo_game_name.png",
                        "./assets/mainmenu/logo_game_name.png", 507, 131)

mixer.fadeout(10000)
run = success
while run:
    clock.tick(fps)

    mouse_pos = pygame.mouse.get_pos()
    btn_login.isHovered(mouse_pos)
    btn_register.isHovered(mouse_pos)
    btn_setting.isHovered(mouse_pos)
    logo_game_name.isHovered(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_login.checkForInput(mouse_pos):
                print("Onclicked-login")
                mixer.music.pause() # pause bgm

                gameScreen = GameScreen()
            if btn_register.checkForInput(mouse_pos):
                print("Onclicked-register")
            if btn_setting.checkForInput(mouse_pos):
                print("Onclicked-setting")

    success, video_image = video.read()

    if success:
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
    else:
        video = cv2.VideoCapture("./assets/mainmenu/effect0.mov")

    window.blit(video_surf, (0, 0))
    btn_login.draw()
    btn_register.draw()
    btn_setting.draw()
    logo_game_name.draw()

    pygame.display.flip()

pygame.quit()
exit()
