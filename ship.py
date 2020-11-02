import pygame
from pygame.locals import *

screen = Rect(0, 0, 800, 900)
shot_reload = 0

clock = pygame.time.Clock()


class Ship(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('images/Corellian.png')
        self.image = pygame.transform.scale(self.image, (80,110))
        self.rect = self.image.get_rect(center = (400, 830))
       
        
    
    def update(self):
        global shot_reload
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            self.rect.move_ip(-8, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(8, 0)
        if key[K_UP]:
            self.rect.move_ip(0, -8)
        if key[K_DOWN]:
            self.rect.move_ip(8, 1)
        if key[K_SPACE] and shot_reload <= 0:
            
            shot_reload = 10 # wait 15 frames before allowing next shot
            sound = pygame.mixer.Sound('sounds/laser_gun_shot.wav')
            sound.play()
            shot = Shot(self.rect.midtop)
        shot_reload -= 1
        self.rect.clamp_ip(screen)        
        

    
class Shot(pygame.sprite.Sprite):

    def __init__(self, pos, xspeed = 0):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('images/shot.bmp')
        self.image = pygame.transform.scale(self.image, (5,7))
        self.rect = self.image.get_rect(midbottom = pos)
        self.xspeed = xspeed

    def update(self):
        self.rect.move_ip(self.xspeed, -20)
        if not screen.contains(self.rect):
            self.kill()



        
        
