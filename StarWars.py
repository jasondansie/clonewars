import sys, pygame, classes, screen_func, random
from pygame.locals import *

from screen_func import *
from classes import Ship
from classes import Shot
from classes import Asteroid


num_asteroids = 0
asteroid_reload = 30


#makes sprite containers and initializes the sprites

ship_container = pygame.sprite.Group()
Ship.containers = ship_container
ship = Ship()

shot_container = pygame.sprite.Group()
Shot.containers = shot_container

asteroid_container = pygame.sprite.Group()
Asteroid.containers = asteroid_container
asteroid_reload = 30

pygame.init()
pygame.mixer.init()


ret = screen_func.intro_screen()
stop = 1
while stop != 0:
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_q:
            exit()
        elif event.type == KEYDOWN and event.key == K_RETURN:
           stop = 0

        
    screen = ret[0]
    background = ret[1]
    
    
    screen.blit(background,(0,150))
    
    pygame.display.flip()                


ret = screen_func.play_screen()                
stop = 1
while stop != 0:
    random_x = random.randint(-2,2)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_q:
            exit()
        elif event.type == KEYDOWN and event.key == K_RETURN:
           stop = 0

    
    screen = ret[0]
    background = ret[1]

    
    if asteroid_reload:
        asteroid_reload = asteroid_reload - 1
    else:
        asteroid = Asteroid(random_x)
        asteroid_reload = 40
        num_asteroids += 1

    #collision detection
    for asteroid in pygame.sprite.spritecollide(ship, asteroid_container, 1):
        ship.kill()
        asteroid.kill()
        stop =0
            
        
    for asteroid in pygame.sprite.groupcollide(shot_container, asteroid_container, 1, 1):
        asteroid.kill()
           
    
    asteroid_container.clear(screen, background)
    shot_container.clear(screen, background)

    #updates all the sprite groups
    ship_container.update()
    shot_container.update()
    asteroid_container.update()

    #draws the background
    screen.blit(background,(0,0))

    #draws the sprites
    ship_container.draw(screen)
    shot_container.draw(screen)
    asteroid_container.draw(screen)
    
    clock.tick(40)
    pygame.display.update()
                       

ret = screen_func.end_screen()
stop = 1
while stop != 0:
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_q:
            exit()
        

    
    screen = ret[0]
    background = ret[1]

    gameover_font = pygame.font.SysFont("arial", 60)
    msg = "Game Over"
    text = gameover_font.render(msg, True, (0,255,0))
    gameover_rect = text.get_rect()
    gameover_rect.centerx = screen.get_rect().centerx
    gameover_rect.centery = screen.get_rect().centery

    quit_font = pygame.font.SysFont("arial", 30)
    quit_msg = "Press ESC to quit" 
    quit_surface = quit_font.render(quit_msg, True, (0,255,0))
    

        
    ship_container.clear(screen, background)
    asteroid_container.clear(screen, background)
    screen.blit(background,(0,0))
    screen.blit(text, (gameover_rect))
    screen.blit(quit_surface, (300, 0))
    
    pygame.display.update()                


