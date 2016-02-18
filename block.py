# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:39:40 2016

@author: renan
"""

"""
                *** Block ***
    
    y-axis
       ^
       |
       |              top
y2   --|--         ----------
       |           |        |
       |      back |        | front
       |           |        |
y1   --|--         ----------
       |             bottom
       |
     --|---------  | ------ | ------------> x-axis
       |           x1       x2
                              
"""

class Block(object):
    def __init__(self,y1_line,y2_line,tunnelLineWidth):
        self.size = 90
        
        self.x1 = 50
        self.x2 = self.size + self.x1        
    
        self.y1 = [(y1_line), (y2_line+self.size)]   
        self.y2 = [(self.y1[0]-self.size), (y2_line+tunnelLineWidth)]
        
        self.yRateBlock = [10, 15, 20, 25, 30]
        
    def top (self, y2Block_change):
        return [self.x1, self.x2, y2Block_change]
        
    def bottom (self, y1Block_change):
        return [self.x1, self.x2, y1Block_change]
    
    def front (self, y1Block_change, y2Block_change):
        return [self.x2, y1Block_change, y2Block_change] 