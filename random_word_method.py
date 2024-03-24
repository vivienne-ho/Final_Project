# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:41:47 2024

@author: adrian
"""
import random
def gen_word():
    w_list = ['kitchen','airplane','topaz','jigsaw','zombie','walkway','twelve',
              'cobweb','elephant','scramble','artichoke','coffee','panda','husky',
              'python','machine','dessert','iceberg','clock','northeastern']
    word = random.choice(w_list)
    return word

print(gen_word())