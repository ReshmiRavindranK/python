# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:59:42 2022

@author: reshm
"""
class Student:
    def __init__(self,name1,marks1):
        self.name=name1
        self.marks=marks1
    def did_pass(self):
        if self.marks>=35:
            return " :passed "
        else:
            return  ":failed"
    def get_name(self):
        return self.name
student1=Student("ANU",45)
student2= Student("MANJU",30)
print("Showing results\n ")
print( student1.get_name(),student1.did_pass())
print(student2.get_name(),student2.did_pass())


 