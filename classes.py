import pygame, random
from pygame.locals import *

screen = Rect(0, 0, 800, 900)
shot_reload = 0

clock = pygame.time.Clock()


class Ship(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(self.rand_image())
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
            self.rect.move_ip(0, 8)
        if key[K_SPACE] and shot_reload <= 0:
            
            shot_reload = 20 # wait 15 frames before allowing next shot
            sound = pygame.mixer.Sound('sounds/LAZER.WAV')
            sound.play()
            shot = Shot(self.rect.midtop)
        shot_reload -= 1
        self.rect.clamp_ip(screen)

    def rand_image(self):
        img = ['images/human-fs-2.png', 'images/Corellian.png', 'images/Obi-Wan-starfighter-icon.png', 'images/Naboo-Starfighter-icon.png',
               'images/X-Wing-icon.png', 'images/falcon.png', 'images/anakin-starfighter-icon.png']
        n = len(img)
        i = img[(random.randrange(0,n))]
        return i
        

    
class Shot(pygame.sprite.Sprite):

    def __init__(self, pos, xspeed = 0):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('images/shot.bmp')
        self.image = pygame.transform.scale(self.image, (10,17))
        self.rect = self.image.get_rect(midbottom = pos)
        self.xspeed = xspeed

    def update(self):
        self.rect.move_ip(self.xspeed, -20)
        if not screen.contains(self.rect):
            self.kill()

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, random_x):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(self.rand_image())
        self.image = pygame.transform.scale(self.image, (80,90))
            
        random_location = random.randint(0,900)
        self.rect = self.image.get_rect( center = (random_location, 0))
        self.random_x = random_x
        self.random_y = random.randint(1,5)
    def update(self):
        self.rect.move_ip(self.random_x, self.random_y)

    def rand_image(self):
        img = ['images/1.png', 'images/2.png', 'images/3.png','images/4.png',
               'images/5.png', 'images/draken.png', 'images/438328663414937072.png',
                'images/human-frigate-0.png','images/human-cargo.png','images/tie-fighter.png',
               'images/lightfreighter.png', 'images/phantom.png',
               'images/human-fs-0.png', 'images/human-fs-1.png', 'images/human-pirate.png', 'images/droidroller.png',
               'images/droidtank.png','images/438328663414937072.png','images/tie-fighter.png']
        n = len(img)
        i = img[(random.randrange(0,n))]
        return i

        
        
