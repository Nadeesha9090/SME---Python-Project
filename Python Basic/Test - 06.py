# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:18:45 2018

@author: hp
"""

x = 10
y = 12 

def exampleThilakz():
    print('my first python func')
    x = 2
    y = 3
    
    z = x + y
    print(z)
    
print('outside func THilakz x and y')
print(x)
print(y)

exampleThilakz()

def myAddition(num1, num2):
    print('num1',num1)
    print('num2',num2)
    print ('Addition', num1+num2)
    

myAddition(1,2)
myAddition(4,2)