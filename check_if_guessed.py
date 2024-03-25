#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:56:08 2024

@author: vivienneho
"""

guessed_list = ["A", "B", "C"]
guess = str(input("Guess a letter: "))


def check_if_guessed(guess, guessed_list):
    for item in guessed_list:
        if guess == item:
            print("Letter has already been guessed")
            return True
    guessed_list.append(guess)
    return False

