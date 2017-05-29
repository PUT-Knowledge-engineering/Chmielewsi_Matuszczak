# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:33:28 2017

@author: Lukasz
"""

import json

class DocumentationCreator:
    def __init__(self, filePath):
        self.filePath = filePath
        self.globalJson = []
        
    def addRow(self, dirPath, name, side, phase, histogram, size):
        dict = {}
        dict["dir"] = dirPath
        dict["name"] = name
        dict["side"] = side
        dict["phase"] = phase
        dict["histogram"] = histogram
        dict["size"] = size
        self.globalJson.append(dict)
        
    def saveToFile(self):
        with open(self.filePath, "a") as myfile:
            myfile.write(json.dumps(self.globalJson))
        
    
        
      
        
