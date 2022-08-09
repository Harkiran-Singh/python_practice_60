# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:08:46 2022

@author: Harkiran.Singh
"""

#harkiran.singh@hotmail.com

email = str(input('Enter the email\n'))
"""email_elements = email.split('@')
print(email_elements)
username = email_elements[0]
domain = email_elements[1]
print(f'username is {username} and domain is {domain}')"""

username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f'username is {username} and domain is {domain}')
