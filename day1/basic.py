# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:11:05 2022

@author: reshm
"""

class Car():
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def show(self):
        print("the model is",self.model," and colour is ",self.color)
        
audi=Car("audi a4","blue") 
ferrari=Car("ferrari 448","green") 
audi.show()  
ferrari.show()    