#hangman
import random
import sys


hangman= ['''
 +---+
     |
     |
     |
     |
======''',
'''
 +---+
 |   |
     |
     |
     |
======''',
'''
 +---+
 |   |
 0   |
     |
     |
======''',
'''
 +---+
 |   |
 0   |
 |   |
     |
======''',
'''
 +---+
 |   |
 0   |
/|   |
     |
======''',
'''
 +---+
 |   |
 0   |
/|\  |
     |
======''',
'''
 +---+
 |   |
 0   |
/|\  |
/    |
======''',
'''
 +---+
 |   |
 0   |
/|\  |
/ \  |
======''',
'''''']
#20 animal names 

words = ['cat','dog','penguin','alligator','camel','goat','puffin','chicken',
         'dolphin','lion','Elephant','horse','pelican','beetle','tiger',
         'spider','snake','shark','whale','monkey',]


word = words[random.randrange(len(words))]
l = len(word)
dash=''
index = []
wrong=0

for i in range(l):
        dash+='-'

while True:
    print('The word is a ', l,'letter word')
    print(dash)
    for i in range(len(word)):
        guess = input('guess a letter: ')
        if str(guess) in word:
            ind = word.index(guess)
            
            if word.count(guess) == 1: 
                dash = dash[:ind] + word[ind] + dash[ind+1:]
                print(dash)
                
            if word.count(guess)>1:
                for i in range(len(word)):
                    if word[i] == guess:
                        index.append(i)
                for j in index:
                        if index[0]==0:
                                dash = dash.replace(dash[0],guess,1)
                        dash = dash[:j] + word[ind] + dash[j+1:]
                index.clear()
                print(dash)

        if dash == word:
            sys.exit('Whatever')
            
        if guess not in word:
            print(hangman[wrong])
            wrong+=1
            if len(hangman) ==wrong+1:
                print(word)
                sys.exit('You are trash bruh')


