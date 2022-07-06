import pygame
from pygame import mixer
from loginScreen import LoginScreen
# from lifeAfterDead import lifeAfterDead
if __name__ == '__main__':
    pygame.init()
    logo = pygame.image.load('./assets/logo.png')
    pygame.display.set_caption("Game Title")
    pygame.display.set_icon(logo)

    # open video player as background
    # pygame.mixer.init()
    # pygame.mixer.music.load('./assets/mainmenu/bgm.mp3')
    # pygame.mixer.music.play(-1, fade_ms=5000)

    mixer.Channel(0).play(mixer.Sound(
        './assets/mainmenu/bgm.mp3'), -1, fade_ms=5000)
    mixer.Channel(0).pause()

    mixer.Channel(1).play(mixer.Sound(
        './assets/sound_bgm/PixelTime.mp3'), -1, fade_ms=5000)
    mixer.Channel(1).pause()

    mixer.Channel(2).play(mixer.Sound(
        './assets/sound_bgm/Crossfire(HardArrange).mp3'), -1, fade_ms=5000)
    mixer.Channel(2).pause()

    mixer.Channel(0).unpause()

    LoginScreen()
    # lifeAfterDead(LoginScreen)
