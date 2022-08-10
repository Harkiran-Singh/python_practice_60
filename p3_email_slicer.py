# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:08:46 2022

@author: Harkiran.Singh
"""

#harkiran.singh@hotmail.com

email = str(input('Enter the email \n'))
"""email_elements = email.split('@')
print(email_elements)
username = email_elements[0]
domain = email_elements[1]
print(f'username is {username} and domain is {domain}')"""


def email_slicer(email):
    no_of_attherate = []
    valid_domain_suffix = {'.com', '.ca', '.org', '.in'}
    for x in email:
        if x == '@':
            no_of_attherate.extend(x)
    if len(no_of_attherate) != 1:
        print('invalid email')
    else:
        username = email[:email.index('@')]
        domain = email[email.index('@')+1:]
        if domain.find('.') == -1:
            print("invalid domain")
        else:
            domain_suffix = domain[domain.index('.'):]
            print(domain_suffix)
            if domain_suffix in valid_domain_suffix:
                print(f'username is {username} and domain is {domain}')
            else:
                print("domain not in list of accepted domains")

email_slicer(email)