# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:40:02 2016

@author: renan
"""


"""
          *** Tunnel ***
    
      -------------------------- y2_line

            O -----
              |   |
              -----          
      -------------------------- y1_line

"""

class Tunnel(object):
    def __init__(self, displayWidth, displayHight):
        self.size = 100
        
        self.lineWidth = 10
        self.lineLength = displayWidth

        self.y1_line = (displayHight/2) + self.size
        self.y2_line = (displayHight/2) - self.size