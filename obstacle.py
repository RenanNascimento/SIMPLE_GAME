# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:29:45 2016

@author: renan
"""

import random

"""
              *** Obstacle ***

     y-axis
       ^
       |
       |            top
y2   --|--         ------
       |           |    |
       |           |    |
       |           |    |
       |     front |    | back
       |           |    |
       |           |    |
y1   --|--         ------
       |           bottom     
       |
       |
     --|--------- | ---- | ------------> x-axis
       |         x1     x2
                              
""" 


class Obstacle(object):
    def __init__(self, displayWidth, y2block):   
        self.decrement = 20
        
        self.hight = 90
        self.len = [20, 100]
        self.dist_btwn_obstacles = [displayWidth+40, displayWidth+100]

        self.y2 = [y2block[0], y2block[1]]
        self.x1 = self.dist_btwn_obstacles[random.randrange(0, 2)]        
        
        self.length = self.len[random.randrange(0, 2)]
        
        self.top_bottom = self.y2[random.randrange(0, 2)]
        
        self.x2 = self.x1 + self.length
        self.y1 = self.top_bottom + self.hight


    def top (self, x1_change):
        return [x1_change, x1_change+self.length, self.top_bottom]
        
    def bottom (self, x1_change):
        return [x1_change, x1_change+self.length, self.y1]

    def front (self, x1_change):
        return [x1_change, self.y1, self.top_bottom]
        