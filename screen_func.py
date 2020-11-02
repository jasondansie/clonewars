import pygame, sys, ship
from pygame.locals import *
from ship import *


screen = Rect(0, 0, 800, 900)
size = width, height = 800,900
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clone Wars Adventure")
    
def intro_screen():
   
    pygame.init()
   

    introsound = pygame.mixer.Sound('sounds/sw_theme.wav')
    introsound.play()
    
     
    background = pygame.image.load("images/CWars_Ad.png").convert()
    background = pygame.transform.scale(background, (800,600))

    return (screen, background)

    

def play_screen():
   

    pygame.mixer.stop()
    sound = pygame.mixer.Sound('sounds/duel remix.wav')
    sound.play()
    # sound1 = pygame.mixer.Sound('sounds/LOCK_S.WAV')
    #  sound1.play()

    background = pygame.image.load("images/back.jpg").convert()
    background = pygame.transform.scale(background, (800,900))
    return (screen, background)


def end_screen():
   
    
    pygame.mixer.stop()
    sound = pygame.mixer.Sound('sounds/darkside.wav')
    sound.play()

    
    
    background = pygame.image.load("images/back.jpg").convert()
    background = pygame.transform.scale(background, (800,900))

    
    
    return (screen, background)

    
           
   

