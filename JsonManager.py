# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:33:28 2017

@author: Lukasz
"""
import json

class JsonManager:
    def __init__(self, filePath):
        self.filePath = filePath
        self.globalJson = []
        
    def addRow(self, contextObject):
        self.globalJson.append(contextObject)
        
        
    def saveToFile(self):
        with open(self.filePath, "w") as myfile:
            myfile.write(json.dumps(self.globalJson))



