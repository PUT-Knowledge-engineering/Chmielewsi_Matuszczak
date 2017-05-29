# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:41:13 2017

@author: Lukasz
"""





import os


class DataManager:
    def __init__(self, sourcePath):
        self.sourcePath = sourcePath
        self.getContextsObjects()
                    
    def getContextsObjects(self):
        for dirName in os.listdir(self.sourcePath):
            for subDirName in os.listdir(self.sourcePath+"/"+dirName):
                singleExamination = [] #tablica wartosci dla jednego badania
                for singleExam in os.listdir(self.sourcePath+"/"+dirName+"/"+subDirName):
                    if singleExam.split(".")[1] == "jpg":
                        singlePhoto = Context(self.sourcePath+"/"+dirName+"/"+subDirName, singleExam)
                        singleExamination.append(singlePhoto)
                self.flowOperation(singleExamination)

                
    def flowOperation(self, contextsArray):
        for k in contextsArray:
            k.fillData("qwe","zxc",[1,2,3],"wer")
            #TO DO - operacje zwiazane z wypelnieniem info o danym zdjeciu
        self.saveJSON(contextsArray)
       

        
    def saveJSON(self, arrayOfContext):
        jsonManager = JsonManager(arrayOfContext[0].dirPath + "/out.txt")
        for o in arrayOfContext:
            jsonManager.addRow(o.createDictionary())
        jsonManager.saveToFile()
        
    
        
x = DataManager("./dane_testowe1")


            
        




    
    
