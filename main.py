import pygame, sys
from pygame.locals import *
import const
from game import Game

pygame.init()
background = pygame.image.load(const.BACKGROUND_IMAGE)
DISPLAYSURF = pygame.display.set_mode((const.GAME_WIDTH_SIZE, const.GAME_HEIGHT_SIZE))
game = Game(DISPLAYSURF)

while True:
    for event in pygame.event.get():
        game.quitControl(event)

        # pause control
        game.pauseControl(event)

    if game.getStart():
        game.drawStartSurface()
        for event in pygame.event.get():
            game.startControl(event)
            game.quitControl(event)
    else:
        # pause hint surface
        if game.getPause():
            game.drawPauseSurface()
            for event in pygame.event.get():
                game.quitControl(event)
                game.pauseControl(event)
                game.restartControl(event)

        else:
            # common logic
            game.update()
            DISPLAYSURF.fill((0, 0, 0))
            DISPLAYSURF.blit(background, (0, 0))
            game.drawMain()
            if game.getGameOver():
                game.drawRestartButton(10, 30)
            game.drawPauseButton()

    pygame.display.update()