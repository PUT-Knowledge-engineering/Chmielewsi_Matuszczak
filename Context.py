# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:54:21 2017

@author: Lukasz
"""
#import cv2

class Context:
    def __init__(self, dirPath, name):
        self.dirPath = dirPath
        self.name = name
        self.path = dirPath + "/" + name
    
    def fillData(self,side, phase, histogram, size):
        self.side = side
        self.phase = phase
        self.histogram = histogram
        self.size = size
        
    def createDictionary(self):
        dict = {}
        dict["dir"] = self.dirPath
        dict["name"] = self.name
        dict["side"] = self.side
        dict["phase"] = self.phase
        dict["histogram"] = self.histogram
        dict["side"] = self.side
        return dict
    
        
        
        