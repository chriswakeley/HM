import math
import pygame
import pygame.gfxdraw
from corridor import *

class Player:
   
    #player variables
    xpos = 0
    ypos = 0
    theta = 0
    color = []
    background = 0
    time = []
    size = 0
    speed = 0
    lastTime = 0
    initspeed = 0
    corridor = None
    arena_walls = None
   
    #aim vars
    aim = False
    rotdir = False
    aimStartTime = 0
    totalAimTime = 1500
    aimAngle = 0
   
    #launch vars
    launch = False
    launchStartTime = 0
   
   
    score = 0
   
    #player init method
    def __init__(self, xpos, ypos, theta, size, speed, color, background, time, arena_walls):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.background = background
        self.theta = theta
        self.time = time
        self.lastTime = time[0]
        self.size = size
        self.speed = speed
        self.initspeed = speed
        self.arena_walls = arena_walls
        self.corridor = corridor((xpos, ypos), theta, time, background, arena_walls)
   
    #player update method moves the player object "movement" amount each times its called in "theta" direction   
    def update(self):
   
        if(self.aim and not self.launch):
            if(self.aimStartTime == 0):
                self.aimStartTime = self.time[0]
           
            direction = 0
           
            if(self.rotdir):
                direction = 1
            else:
                direction = -1
               
            aimTimeDiff = self.time[0] - self.aimStartTime
           
            if(aimTimeDiff >= self.totalAimTime):
                self.aimStartTime = 0   
            else:   
                self.aimAngle = self.theta + math.pow(aimTimeDiff, 2) * (math.pi*2) / (math.pow(self.totalAimTime, 2)) * direction
        else:
            self.aimStartTime = 0
           
        if(self.launch):
            self.aim = False
            if(self.launchStartTime == 0):
                self.launchStartTime = self.time[0]
                self.theta = self.aimAngle
                self.speed = self.initspeed * 2
                self.corridor = corridor((self.xpos, self.ypos), self.theta, self.time, self.background, self.arena_walls)
               
            timediff = self.time[0] - self.launchStartTime
            if(timediff >= 500):
                self.launch = False
                self.speed = self.initspeed
               
        else:
            self.launchStartTime = 0
           
           
           
        timediff = self.time[0] - self.lastTime
        self.lastTime = self.time[0]
       
        movement = timediff * self.speed
        self.xpos = self.xpos + math.cos(self.theta)* movement
        self.ypos = self.ypos + math.sin(self.theta)* movement
       
        self.draw()#redraw
        self.corridor.update()
   
    #draws the shape representing the player based on the current coordinates.   
    def draw(self):
       
        sides = self.score + 3
       
        tempTheta = self.theta
        thetaInc = (math.pi*2)/sides
       
        points = []
       
        #calculating the verticies for the shape.
        for i in range(0, sides):
            xtemp = self.xpos + math.cos(tempTheta)*self.size
            ytemp = self.ypos + math.sin(tempTheta)*self.size
            tempTheta += thetaInc
           
            points.append([xtemp, ytemp])
       
        #draw the ploygon   
        pygame.gfxdraw.aapolygon(self.background, points, self.color)
       
        if(self.aim):
            tempX = int(self.xpos + math.cos(self.aimAngle)* 100)
            tempY = int(self.ypos + math.sin(self.aimAngle)* 100)
            pygame.gfxdraw.line(self.background, int(self.xpos), int(self.ypos), tempX, tempY, self.color)
   
   
    def setAim(self, aimvar):
        self.aim = aimvar
    def setLaunch(self, launchvar):
        self.launch = launchvar
    def setDir(self, dirvar):
        self.rotdir = dirvar
    def getAim(self):
        return self.aim
    def getLaunch(self):
        return self.launch
