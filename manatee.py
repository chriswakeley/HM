import pygame
import os
import math

from pygame.locals import *
from arena import *
from corridor import *
from Player import *
from geometry import *

BLACK = (0, 0, 0)
width = height = 800
BORDER_WIDTH = 70
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
HITBOX = 20
CALIBRATION = 100
p1score = 0
p2score = 0


def main(): 

    ### PyGame init   
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("Arial", 16)
   
    #load music
    pygame.mixer.music.load('paniq - Neurons- Fire At Will - 11 I Love Only You.mp3')
   
    #Fill background
    mainsurface = pygame.Surface(screen.get_size())
    mainsurface = mainsurface.convert()
    mainsurface.fill(BLACK)
   
    #clock
    clock = pygame.time.Clock()
    FRAMES_PER_SECOND = 60
    time = [0]
   
    #setup arena walls
    game_arena = arena( (((BORDER_WIDTH, BORDER_WIDTH), (width-BORDER_WIDTH, BORDER_WIDTH)), ((BORDER_WIDTH, BORDER_WIDTH), (BORDER_WIDTH, height-BORDER_WIDTH)), ((width-BORDER_WIDTH, BORDER_WIDTH), (width-BORDER_WIDTH, height-BORDER_WIDTH)), ((BORDER_WIDTH, height-BORDER_WIDTH), (width-BORDER_WIDTH, height-BORDER_WIDTH))), time, mainsurface)
    #arena = arena((((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0))), time, mainsurface)
   
   
    #Setup player objects
    #player variables
    p1score = 0
    p2score = 0
    '''
    launch1 = []
    launch1.append(False)
    aim1 = []
    aim1.append(False)
    aim1.append(False)
    '''
    p1 = Player(250, 250, math.pi/2, 20, .1, GREEN, mainsurface, time, game_arena.arena_walls)
   
    '''
    launch2 = [];
    launch2.append(False)
    aim2 = [];
    aim2.append(False)
    aim2.append(False)
    '''
    p2 = Player(550, 550, -math.pi/2, 20, .1, RED, mainsurface, time, game_arena.arena_walls)
   
   
    #Blit everything to the screen
    screen.blit(mainsurface, (0, 0))
    pygame.display.flip()

    #Testing
    #corridor1 = corridor([[[0, 20], [600, 120]], [[0, 120], [600, 220]]], time, mainsurface)
    heading = math.pi/4
   
    #play music
    pygame.mixer.music.play(0)
   
    # Event loop
    while 1:
        heading = heading - 0.01
       
        #control the loop to 60fps
        #time[0] = time[0] + clock.tick_busy_loop(FRAMES_PER_SECOND)
        clock.tick_busy_loop(FRAMES_PER_SECOND)
        time[0] = pygame.time.get_ticks() + CALIBRATION
       
        #fill the background
        mainsurface.fill(BLACK)
        #corridor1 = corridor((200, 300), heading*2, time, mainsurface, game_arena.arena_walls)
        #corridor2 = corridor((200, 200), heading*1.2, time, mainsurface, game_arena.arena_walls)
        ###############COLLISION CHECKING######################
        #setup collision line for players
        p1collision = (p1.xpos + math.cos(p1.theta)*HITBOX, p1.ypos + math.sin(p1.theta)*HITBOX)
        p2collision = (p2.xpos + math.cos(p2.theta)*HITBOX, p2.ypos + math.sin(p2.theta)*HITBOX)
        collided = False
        #pygame.draw.aaline(mainsurface, GREEN, (p1.xpos, p1.ypos), p1collision, True)
        #check collisions for player 1
       
        for i in range(0, 4):
            intersect = line_seg_intersect((p1.xpos, p1.ypos), p1collision, game_arena.arena_walls[i][0], game_arena.arena_walls[i][1])
            if intersect != None:
                p2score = p2score + 1
                collided = True
               
        intersect = line_seg_intersect((p1.xpos, p1.ypos), p1collision, p2.corridor.walls[0][0], p2.corridor.walls[0][1])
        if intersect != None:
            p2score = p2score + 1
            collided = True
           
        intersect = line_seg_intersect((p1.xpos, p1.ypos), p1collision, p2.corridor.walls[1][0], p2.corridor.walls[1][1])
        if intersect != None:
            p2score = p2score + 1
            collided = True
               
        for i in range(0, 4):
            intersect = line_seg_intersect((p2.xpos, p2.ypos), p2collision, game_arena.arena_walls[i][0], game_arena.arena_walls[i][1])
            if intersect != None:
                p1score = p1score + 1
                collided = True
               
        intersect = line_seg_intersect((p2.xpos, p2.ypos), p2collision, p1.corridor.walls[0][0], p1.corridor.walls[0][1])
        if intersect != None:
            p1score = p1score + 1
            collided = True
        intersect = line_seg_intersect((p2.xpos, p2.ypos), p2collision, p1.corridor.walls[1][0], p1.corridor.walls[1][1])
        if intersect != None:
            p1score = p1score + 1
            collided = True
      
        if collided:
            p1, p2 = endround()
        ##############INPUT INTERPRETATION#####################
        for event in pygame.event.get():
            if event.type == QUIT:
                return
       
        #checking pressed keys
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not p1.getLaunch():
            p1.setAim(True)
            p1.setDir(False)
          
        elif key[pygame.K_RIGHT] and not p1.getLaunch():
            p1.setAim(True)
            p1.setDir(True)
        else:
            p1.setAim(False)
          
        if key[pygame.K_UP] and p1.getAim() and not p1.getLaunch():
            FREQUENCY = 444.44
            freq_ratio = 1.0*(time[0] % FREQUENCY)/FREQUENCY
            if(freq_ratio <= 0.4):
                p1.setLaunch(True)
          
        if key[pygame.K_a] and not p2.getLaunch():
            p2.setAim(True)
            p2.setDir(False)
          
        elif key[pygame.K_d] and not p2.getLaunch():
            p2.setAim(True)
            p2.setDir(True)
        #else:
            #p2.setAim(False)
          
        if key[pygame.K_w] and p2.getAim() and not p2.getLaunch():          
            FREQUENCY = 444.44
            freq_ratio = 1.0*(time[0] % FREQUENCY)/FREQUENCY
            if(freq_ratio <= 0.4):
                p2.setLaunch(True)

      
        ####################UPDATE###########################

       
               
        #########################RENDERING#################################
        #circle1ani.blit(background, (mapObjects[1].xPos-118, mapObjects[1].yPos-108))
        #ground.blit(background, (0, 445))
        #rground.blit(background, (445, 0))
        #lground.blit(background, (0, 0))
        #player1ani.blit(background, (Player1Model.body.xPos -24, Player1Model.body.yPos -21))
        #player2ani.blit(background, (Player2Model.body.xPos -24, Player2Model.body.yPos -21))
        p1.update()
        p2.update()
        #corridor1.update()
        #corridor2.update()
        game_arena.update()
        screen.blit(mainsurface, (0, 0)) 
        #draw_space(screen, space)
        pygame.display.update()
       
        def endround():
            i = pygame.time.get_ticks()
           
            while (pygame.time.get_ticks() - i) < 888:
               a = 0
            p1 = Player(250, 250, math.pi/2, 20, .1, GREEN, mainsurface, time, game_arena.arena_walls)
            p1.score = p1score
            p2 = Player(550, 550, -math.pi/2, 20, .1, RED, mainsurface, time, game_arena.arena_walls)
            p2.score = p2score
            print p1.ypos
            print p2.ypos
            print "***"
            return p1, p2

        '''
        def endround():
            print "round ended"
            p1 = Player(100, 100, math.pi/2, 20, .1, GREEN, mainsurface, time, game_arena.arena_walls)
            p1.score = p1score
            p2 = Player(500, 500, math.pi/2, 20, .1, GREEN, mainsurface, time, game_arena.arena_walls)
            p2.score = p2score
        '''

if __name__ == '__main__': main()    
