import math
import pygame
from geometry import *



class corridor:
    FREQUENCY = 444.44
    WALL_OFFSET = 10
    arena_walls = None
    walls = [[[None, None], [None, None]], [[None, None], [None, None]]]
    time = None
    mainsurface = None
    
    def __init__(self, pos, heading, time, mainsurface, arena_walls):
        self.walls = [[[None, None], [None, None]], [[None, None], [None, None]]]
        self.time = time
        self.mainsurface = mainsurface
        self.arena_walls = arena_walls
        #print self.arena_walls
        #calculate a point on wall 1
        offset_angle = heading - math.pi/2
        wall_origin = ((pos[0] + math.cos(offset_angle)*self.WALL_OFFSET), (pos[1] + math.sin(offset_angle)*self.WALL_OFFSET))
        
        wall_point1 = (int((wall_origin[0] + math.cos(heading)*3000)), int((wall_origin[1] + math.sin(heading)*3000)))
        wall_point2 = (int((wall_origin[0] + math.cos(heading)*-3000)), int((wall_origin[1] + math.sin(heading)*-3000)))
        #print wall_point1
        #print wall_point2
        #pygame.draw.aaline(self.mainsurface, GREEN, wall_point1, wall_point2, True)
        #calculate intersections with arena walls to obtain end points
        for i in range(0, 4):
            intersect = line_seg_intersect(wall_point1, wall_point2, self.arena_walls[i][0], self.arena_walls[i][1])
            #print intersect
            
            if intersect != None:
                if self.walls[0][0][0] == None and self.walls[0][0][1] == None:     
                               
                    self.walls[0][0][0] = int(intersect[0])
                    self.walls[0][0][1] = int(intersect[1])
               
                else:
                    
                    self.walls[0][1][0] = int(intersect[0])
                    self.walls[0][1][1] = int(intersect[1])

        
        #calculate a point on wall 2            
        offset_angle = heading + math.pi/2
        wall_origin = ((pos[0] + math.cos(offset_angle)*self.WALL_OFFSET), (pos[1] + math.sin(offset_angle)*self.WALL_OFFSET))
        
        wall_point1 = (int((wall_origin[0] + math.cos(heading)*3000)), int((wall_origin[1] + math.sin(heading)*3000)))
        wall_point2 = (int((wall_origin[0] + math.cos(heading)*-3000)), int((wall_origin[1] + math.sin(heading)*-3000)))
        #print wall_point1
        #print wall_point2
        #pygame.draw.aaline(self.mainsurface, GREEN, wall_point1, wall_point2, True)
        #print wall_origin
        #print wall_origin2
        #pygame.draw.aaline(self.mainsurface, GREEN, wall_origin, wall_origin2, True)
        #calculate intersections with arena walls to obatin end points
        for i in range(0, 4):
            intersect = line_seg_intersect(wall_point1, wall_point2, self.arena_walls[i][0], self.arena_walls[i][1])
            #print intersect
            if intersect != None:

                if self.walls[1][0][0] == None and self.walls[1][0][1] == None:
                    #print "setting first coord"
                    self.walls[1][0][0] = int(intersect[0])
                    self.walls[1][0][1] = int(intersect[1])

                else:
                    #print "setting second coord"  
                    self.walls[1][1][0] = int(intersect[0])
                    self.walls[1][1][1] = int(intersect[1])


        
    def update(self):
        self.draw()
            
    def draw(self):

        freq_ratio = 1.0*(self.FREQUENCY-self.time[0]%self.FREQUENCY)/self.FREQUENCY
        wall_color = ((100 + math.pow(freq_ratio*5, 3)), (200 - math.pow(freq_ratio*5, 3)), (100 + math.pow(freq_ratio*5, 3)))

        if self.walls[0][0] != [None, None] and self.walls[0][1] != [None, None]:
            pygame.draw.aaline(self.mainsurface, wall_color, self.walls[0][0], self.walls[0][1], True)
            
        if self.walls[1][0] != [None, None] and self.walls[1][1] != [None, None]:
            pygame.draw.aaline(self.mainsurface, wall_color, self.walls[1][0], self.walls[1][1], True)

    
