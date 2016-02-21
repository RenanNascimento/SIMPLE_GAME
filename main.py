# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:23:06 2016

@author: renan
"""

import pygame

from block import Block
from tunnel import Tunnel
from obstacle import Obstacle    

#Global variables
class gl:
    
    loopRange = 20   
    
    """
    Window
    """
    displayWidth = 1000
    displayHight = 600  
    
    """
    Colors - RGB
    """
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    blue = (0,0,255)

    """
    Time
    """
    FPS = 60

    """
    Tunnel
    """
    tunnel = Tunnel(displayWidth, displayHight)

    """
    Block
    """
    block = Block(tunnel.y1_line, tunnel.y2_line,tunnel.lineWidth)
    y2Block_change = block.y2[0]
    y1Block_change = y2Block_change + block.size    
    
    """
    Obstacle
    """
    obstacle = []
    obstacleDist = 300
    
    """
    Game Play
    """
    pause = False

def drawTunnel():    
    
    pygame.draw.rect(gameDisplay, gl.white, [0, gl.tunnel.y1_line, gl.tunnel.lineLength, gl.tunnel.lineWidth])
    pygame.draw.rect(gameDisplay, gl.white, [0, gl.tunnel.y2_line, gl.tunnel.lineLength, gl.tunnel.lineWidth])

def drawBlock():    
   
    pygame.draw.rect(gameDisplay, gl.blue, [gl.block.x1, gl.y2Block_change, gl.block.size, gl.block.size])

    
def drawObstacle(indexLastObstacle):

#    if gl.obstacle == []:
#        gl.obstacle.append(Obstacle(gl.displayWidth,gl.block.y2))
#    if not gl.pause:
#        gl.obstacle[0].x1 = gl.obstacle[0].x1 - gl.obstacle[0].decrement
#        
#    pygame.draw.rect(gameDisplay, gl.white, [gl.obstacle[0].x1,\
#                                      gl.obstacle[0].top_bottom,\
#                                      gl.obstacle[0].length,\
#                                      gl.obstacle[0].hight])   

    if gl.obstacle == []:
        gl.obstacle.append(Obstacle(gl.displayWidth,gl.block.y2))
    elif(gl.displayWidth - gl.obstacle[indexLastObstacle].x1 >= gl.obstacleDist):
            gl.obstacle.append(Obstacle(gl.displayWidth,gl.block.y2))  
            indexLastObstacle = indexLastObstacle + 1            
            
    for i in range(len(gl.obstacle)):
        if not gl.pause:
            gl.obstacle[i].x1 = gl.obstacle[i].x1 - gl.obstacle[i].decrement
        pygame.draw.rect(gameDisplay, gl.white, [gl.obstacle[i].x1,\
                                          gl.obstacle[i].top_bottom,\
                                          gl.obstacle[i].length,\
                                          gl.obstacle[i].hight])

    if gl.obstacle[0].x1 <= -100:
        gl.obstacle.pop(0)
        indexLastObstacle -= 1

    return indexLastObstacle

def yChangeRateBlock(y_auxBlock):
    
    if y_auxBlock == 1 and gl.y2Block_change != gl.block.y2[1]:
        gl.y1Block_change -= gl.block.yRateBlock
        gl.y2Block_change -= gl.block.yRateBlock
    elif y_auxBlock == 0 and gl.y2Block_change != gl.block.y2[0]:
        gl.y1Block_change += gl.block.yRateBlock
        gl.y2Block_change += gl.block.yRateBlock

def collision():

    for i in range(len(gl.obstacle)):
        #Block
        frontBlock = gl.block.front(gl.y1Block_change, gl.y2Block_change)
        topBlock = gl.block.top(gl.y2Block_change)        
        bottomBlock = gl.block.bottom(gl.y1Block_change)
        #Obstacle
        frontObstacle = gl.obstacle[i].front(gl.obstacle[i].x1)
        topObstacle = gl.obstacle[i].top(gl.obstacle[i].x1)
        bottomObstacle = gl.obstacle[i].bottom(gl.obstacle[i].x1)
        if(frontBlock[0] == frontObstacle[0]):
            if((frontBlock[1] <= frontObstacle[1] and \
               frontBlock[1] >= frontObstacle[2] and \
               frontBlock[2] <= frontObstacle[2]) or \
               (frontBlock[1] >= frontObstacle[1] and \
               frontBlock[2] >= frontObstacle[2] and \
               frontBlock[2] <= frontObstacle[1])): 
                freeze()
        elif(topBlock[2] == bottomObstacle[2] or bottomBlock[2] == topObstacle[2]):
            if((topBlock[0] <= bottomObstacle[0] and topBlock[1] >= bottomObstacle[1]) or \
               (topBlock[0] >= bottomObstacle[0] and topBlock[1] <= bottomObstacle[1]) or \
               (topBlock[0] <= bottomObstacle[0] and topBlock[1] >= bottomObstacle[0] and topBlock[1] <= bottomObstacle[1]) or \
               (topBlock[0] >= bottomObstacle[0] and topBlock[0] <= bottomObstacle[1] and topBlock[1] >= bottomObstacle[1])):
                  freeze()

def freeze():
    gl.pause = True

def gameLoop():    
    gameExit = False    
    index = 0
    y_auxBlock = 0
        
    indexLastObstacle = 0    
    
    while not gameExit:
        
        for index in range(gl.loopRange):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit   = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if gl.y2Block_change == gl.block.y2[0]:
                            y_auxBlock = 1
                        elif gl.y2Block_change == gl.block.y2[1]:
                            y_auxBlock = 0
    
            gameDisplay.fill(gl.black)
            if not gl.pause:
                yChangeRateBlock(y_auxBlock)
            drawBlock()     
            drawTunnel()
            indexLastObstacle = drawObstacle(indexLastObstacle)
            collision()
    
            pygame.display.update()

        clock.tick(gl.FPS)

    #Quit
    pygame.quit()
    #Quit python
    quit()


"""
    Pygame Initialization
"""
pygame.init()
gameDisplay = pygame.display.set_mode((gl.displayWidth,gl.displayHight))
pygame.display.set_caption('simple_game')
clock = pygame.time.Clock()        

"""
    Game Engine
"""
gameLoop()



