# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:09:13 2024

@author: adrian
"""

import random

class Hangman():
    
    def __init__(self):
        self.guess_list = []
        
    def gen_word(self):
        w_list = ['kitchen','airplane','topaz','jigsaw','zombie','walkway','twelve',
                  'cobweb','elephant','scramble','artichoke','coffee','panda','husky',
                  'python','machine','dessert','iceberg','clock','northeastern']
        self.word = random.choice(w_list)
        return self.word

    def check_if_guessed(self,guess):
        x = False
        if len(self.guess_list) == 0:
            self.guess_list.append(guess)
            return False
        else:
            for item in self.guess_list:
                if guess == item:
                    x = True
            if x == False:
                self.guess_list.append(guess)
            elif x == True:
                print('Letter has already been guessed.')
            return x
    
    def correct_or_wrong(self,guess):
        decision = False
        for letter in self.word:
            if guess == letter:
                decision = True
        return decision  

    def display_user_guess(self):
        display = []
        answer_list = list(self.word)
        for item in answer_list:
            if item in self.guess_list:
                    display.append(item)
            else:
                display.append("_")
        return display
    
    def end_win_func(self):
        answer_list = list(self.word)
        if answer_list == self.display_user_guess():
            print(f'Congrats! You solved the word "{self.word}"! ')
            return True
        else:
            return False
        
    def end_lose_func(self):
        print(f'Too bad, you ran out of guesses. The correct word was "{self.word}". ')
        
    def man_add(self,guessnum):
        
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

#-----------------------------------------------------------------                    

print('Hello, welcome to our hangman game! ') 
h = Hangman()
h.gen_word()
limit = 0
won = False
count = 1

ready = input('Are you ready to play? ')
if ready == 'yes':
    print('Ok, generating word...done!')
    while limit <= 16 and won == False:
        
        let_guess = input('Enter a letter guess. ')
    
        contin = h.check_if_guessed(let_guess)
            
        if contin == False:
            continue2 = h.correct_or_wrong(let_guess)
            
            if continue2 == True:
                print(h.display_user_guess())
                continue3 = h.end_win_func()
                
                if continue3 == True:
                    won = True
                    
                elif continue3 == False:
                    limit = limit+1
                    
            elif continue2 == False:
                print(h.display_user_guess())
                h.man_add(count)
                limit = limit+1
                count = count+1
    
    if won == False:
        h.end_lose_func()

elif ready == 'no':
    print('Come back again soon! ')
             
    