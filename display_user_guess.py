#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:24:32 2024

@author: vivienneho
"""

answer = "PANDA"
guess_list = ["A", "N", "L"]

def display_user_guess(answer, guess_list):
    display = []
    answer_list = list(answer)
    for item in answer_list:
        if item in guess_list:
            display.append(item)
        else:
            display.append("_")
    print(display)
    
    
display_user_guess(answer, guess_list)