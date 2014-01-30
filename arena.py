import math
import pygame


GREEN = (  0, 255,   0)

class arena:
    FREQUENCY = 444.44
    arena_walls = (((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)))
    time = None
    mainsurface = None
    
    def __init__(self, arena_walls, time, mainsurface):
        self.arena_walls = arena_walls
        self.time = time
        self.mainsurface = mainsurface
    
    def update(self):
        self.draw()
            
    def draw(self):
        freq_ratio = 1.0*(self.FREQUENCY-self.time[0]%self.FREQUENCY)/self.FREQUENCY
        wall_color = ((100 + math.pow(freq_ratio*5, 3)), (50 - math.pow(freq_ratio*3, 3)), (50 - math.pow(freq_ratio*3, 3)))

        pygame.draw.aaline(self.mainsurface, wall_color, self.arena_walls[0][0], self.arena_walls[0][1], True)
        pygame.draw.aaline(self.mainsurface, wall_color, self.arena_walls[1][0], self.arena_walls[1][1], True)
        pygame.draw.aaline(self.mainsurface, wall_color, self.arena_walls[2][0], self.arena_walls[2][1], True)
        pygame.draw.aaline(self.mainsurface, wall_color, self.arena_walls[3][0], self.arena_walls[3][1], True)
        
        point = self.arena_walls[0][0]
        spikenum = 200.0
        for i in range(1, int(spikenum)):
            if i%2 != 0:
                nextpoint = (self.arena_walls[0][0][0] + (self.arena_walls[0][1][0] - self.arena_walls[0][0][0])*((i+1)/spikenum), self.arena_walls[0][0][1] - (math.pow(freq_ratio*3, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.3*spikenum))))
            else:
                nextpoint = (self.arena_walls[0][0][0] + (self.arena_walls[0][1][0] - self.arena_walls[0][0][0])*((i+1)/spikenum), self.arena_walls[0][0][1])
      
            spikecolor = (200 - (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))), 40, 40 + (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))))
            pygame.draw.aaline(self.mainsurface,spikecolor , point, nextpoint, True)
            point = nextpoint
        
        
        point = self.arena_walls[3][0]
        spikenum = 200.0
        for i in range(1, int(spikenum)):
            if i%2 != 0:
                nextpoint = (self.arena_walls[3][0][0] + (self.arena_walls[3][1][0] - self.arena_walls[3][0][0])*((i+1)/spikenum), self.arena_walls[3][0][1] + (math.pow(freq_ratio*3, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.3*spikenum))))
            else:
                nextpoint = (self.arena_walls[3][0][0] + (self.arena_walls[3][1][0] - self.arena_walls[3][0][0])*((i+1)/spikenum), self.arena_walls[3][0][1])
      
            spikecolor = (200 - (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))), 40, 40 + (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))))
            pygame.draw.aaline(self.mainsurface,spikecolor , point, nextpoint, True)
            point = nextpoint
        
        
        point = self.arena_walls[1][0]
        spikenum = 200.0
        for i in range(1, int(spikenum)):
            if i%2 != 0:
                nextpoint = (self.arena_walls[1][0][0] - (math.pow(freq_ratio*3, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.3*spikenum))), self.arena_walls[1][0][1] + (self.arena_walls[1][1][1] - self.arena_walls[1][0][1])*((i+1)/spikenum))
            else:
                nextpoint = (self.arena_walls[1][0][0], self.arena_walls[1][0][1] + (self.arena_walls[1][1][1] - self.arena_walls[1][0][1])*((i+1)/spikenum))
      
            spikecolor = (200 - (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))), 40, 40 + (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))))
            pygame.draw.aaline(self.mainsurface,spikecolor , point, nextpoint, True)
            point = nextpoint
            
        point = self.arena_walls[2][0]
        spikenum = 200.0
        for i in range(1, int(spikenum)):
            if i%2 != 0:
                nextpoint = (self.arena_walls[2][0][0] + (math.pow(freq_ratio*3, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.3*spikenum))), self.arena_walls[2][0][1] + (self.arena_walls[2][1][1] - self.arena_walls[2][0][1])*((i+1)/spikenum))
            else:
                nextpoint = (self.arena_walls[2][0][0], self.arena_walls[2][0][1] + (self.arena_walls[2][1][1] - self.arena_walls[2][0][1])*((i+1)/spikenum))
      
            spikecolor = (200 - (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))), 40, 40 + (math.pow(freq_ratio*5, 3)*(((spikenum/2)-math.fabs(i-(spikenum/2)))/(.4*spikenum))))
            pygame.draw.aaline(self.mainsurface,spikecolor , point, nextpoint, True)
            point = nextpoint
       
            
        
        
        
        
        
    
