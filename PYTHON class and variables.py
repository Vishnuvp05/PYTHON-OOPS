# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:37:38 2022

@author: ADOLF
"""

#PYTHON-OOPS 

#class - blueprint of template ,it occupies a memory space only when an object is created 

#class consists collection of methods and attributes , when a variable is used in class it is called as an attribute

#when a function is created in class it is called as method 

#creating a program code for a supermarket to calculate total cost of a thinga that a customer bought 


class Supermarket:   


    def __init__(self, name ,biscuit , bread , chocolate , soap):   #init is a special method used to reduce no of codes 
        self.name = name    #self is used to point current object and to hold objec
        self.biscuit = 8 * biscuit
        self.bread = 9 * bread
        self.chocolate = 10 * chocolate
        self.soap = 11 * soap


    def items(self):   # class method
        list = f'''customer Name : {self.name}\n Biscuit: {self.biscuit}rs\n Bread : {self.bread}rs
 Chocolate : {self.chocolate}rs\n soap : {self.soap}rs\n'''
        return list

    
cust1 = Supermarket('Vishnu', 1, 1, 7, 2)   #object 1
cust2 = Supermarket( 'Prasath', 1, 2, 6, 7) #object 2


print(cust1.items())
print(cust2.items())
