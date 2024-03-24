# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:11:12 2024

@author: adrian
"""

word = 'waterbottle'
guess = input('What is your letter guess? ')

def correct_or_wrong(word,guess):
    decision = False
    for letter in word:
        if guess == letter:
            decision = True
    return decision  
 
print(correct_or_wrong(word,guess))
        
    