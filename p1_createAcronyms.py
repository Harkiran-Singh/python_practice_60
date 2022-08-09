# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:44:24 2022

@author: Harkiran.Singh
"""

user_input = str(input('Enter a phrase:'))  #store input from user in a variable using input() method
text = user_input.split()                   #split the user_input string into a list using split() method
acr=''                                      #initialize a empty  string called acronym
for x in text:                              #iterate over the list  
    acr=(acr+x[0]).upper()                 # add the first character for each object in the list to the acronym
print(acr)                                  #print the acronym