import pygame

from loginScreen import LoginScreen
# from lifeAfterDead import lifeAfterDead
if __name__ == '__main__':
    pygame.init()
    logo = pygame.image.load('./assets/logo.png')
    pygame.display.set_caption("Game Title")
    pygame.display.set_icon(logo)

    # open video player as background
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/mainmenu/bgm.mp3')
    pygame.mixer.music.play(-1, fade_ms=5000)

    LoginScreen()
    # lifeAfterDead(LoginScreen)
