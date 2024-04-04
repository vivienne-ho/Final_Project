#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Project
Created by: Vivienne Ho and Adrian Serrano
EECE2140
Northeastern University
"""

import random

class Hangman():
    
    def __init__(self):
        self.guessed_list = []
        self.wrongguesses = 0
        self.answer = None
        
    
    def gen_word(self):
        w_list = ['kitchen','airplane','topaz','jigsaw','zombie','walkway','twelve',
              'cobweb','elephant','scramble','artichoke','coffee','panda','husky',
              'python','machine','dessert','iceberg','clock','northeastern']
        answer = random.choice(w_list)
        self.answer = answer        
        
        
    def check_if_guessed(self, guess):
        for item in self.guessed_list:
            if guess == item:
                return True
            self.guessed_list.append(guess)
            return False


    def correct_or_wrong(self, answer):
        decision = False
        for letter in answer:
            if guess == letter:
                decision = True
                return decision  
        self.wrongguesses = self.wrongguesses+1
        return decision
 
    def display_user_guess(self, answer):
        display = []
        answer_list = list(answer)
        for item in answer_list:
            if item in self.guessed_list:
                display.append(item)
            else:
                display.append("_")
        print(display)

    def man_add(guessnum):
        if guessnum == 1:
            print("""
                ________
               /        \ 
              |         |
               \________/ 
               """)
    
        elif guessnum == 2:
            print("""                
                ________
               /        \ 
              |          |
               \________/ 
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |""")
        elif guessnum == 3:
             print("""                
                ________
               /        \ 
              |          |
               \________/ 
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                     \ 
                      \ 
                       \ 
                        \ """)
        elif guessnum == 4:
            print("""                
                ________
               /        \ 
              |          |
               \________/ 
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
                
        elif guessnum == 5:
            print("""                
                ________
               /        \ 
              |          |
               \________/ 
                    |    /
                    |   /
                    |  /
                    | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
                
        elif guessnum == 6:
            print("""                
                ________
               /        \ 
              |          |
               \________/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
        elif guessnum == 7:
            print("""                
                ________
               /  *  *   \ 
              |          |
               \________/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
        elif guessnum == 8:
            print("""                
                ________
               /  *  *   \ 
              |    ^     |
               \________/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
        elif guessnum == 9:
            print("""                
                ________
               /  *  *   \ 
              |    ^     |
               \___V_____/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
        elif guessnum == 10:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ """)
        elif guessnum == 11:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ 
             <SS""")
        elif guessnum == 12:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ 
             <SS         SS>""")
        elif guessnum == 13:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
               \    |    /WW
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ 
             <SS         SS>""")
        elif guessnum == 14:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
             WW\    |    /WW
                \   |   /
                 \  |  /
                  \ | /
                    |
                    |
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ 
             <SS         SS>""")
        elif guessnum == 15:
            print("""                
                
                &&&&&&&&&
              &/  *  *   \& 
             &|    ^     |&
               \___V_____/ 
             WW\    |    /WW
                \   |   /
                 \  |  /
                  \ | /
                    |
            LAST    |    GUESS
                    |
                    |
                   / \ 
                  /   \ 
                 /     \ 
                /       \ 
             <SS         SS>""")
             
        else:
            return
            

class UserGuess(Hangman):
    def __init__(self, guess):
        self.guess = guess
        self.guessed_list = []
        self.wrongguesses = 0

#Game play:
    
game = Hangman()
game.gen_word()
#Make sometype of welcome, instruction, and function to display starting word 
while(1):
    guess = input("Enter a letter guess: ")
    obj1 = UserGuess(guess)
    alreadyguessed = obj1.check_if_guessed(obj1.guess)
    if alreadyguessed == True:
        print("You have already guessed this letter")
    else:
        right = obj1.correct_or_wrong(game.answer)
        # Make sure to print out the graphics
        if right == False:
            obj1.man_add()
        obj1.display_user_guess(game.answer)
        
        
    