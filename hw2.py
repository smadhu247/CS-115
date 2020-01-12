'''Created on 9/19/19
@author: Sanjana Madhu, in collaboration with Michael Gajdosik
Pledge: I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2'''

import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)


# Leave the following lists in place.
scrabbleScores = \
               [ ['a', 1], ['b', 3], ['c', 3], ['d', 2],
                 ['e', 1], ['f', 4], ['g', 2],['h', 4],
                 ['i', 1], ['j', 8], ['k', 5], ['l', 1],
                 ['m', 3], ['n', 1],['o', 1], ['p', 3],
                 ['q', 10], ['r', 1], ['s', 1], ['t', 1],
                 ['u', 1],['v', 4], ['w', 4], ['x', 8],
                 ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble',
              'can', 'foo', 'spam', 'spammy', 'zzyzva']

# Implementation of function

#letterScore outputs the score of a letter based on the scores that correlate with each letter in the list scrabbleScores
def letterScore(letter, scorelist):
    if (letter == ""):
        return 0
    if (letter == scorelist[0][0]):
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

#wordScore outputs the score of a word using the score of each letter 
def wordScore(S, scorelist):
    if (len(S) == 0):
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

#scoreList returns a list of all of the words in the Dictionary that can be made from those letters and the score for each one 
def scoreList (Rack):
   return map(lambda x: [x, wordScore(x, scrabbleScores)], listOfWords(Dictionary, Rack))

#bestWord returns a list with two elements (the highest possible scoring word from that Rack followed by its score)
def bestWord (Rack):
    if scoreList(Rack) == []:
        return ["",0]
    else:
        return reduce(maximum, scoreList(Rack))


#Helper functions
    
#maximum is a helper function of remove
def maximum(x,y):
    if x[1]<y[1]:
        return y
    else:
        return x
#ind is a helper function of remove
def ind(e, L):
    if not L:
        return len(L)
    elif e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])

#remove delets a letter from the Rack
def remove(letter, Rack):
    if not Rack:
        return Rack
    elif letter == Rack[0]:
        return Rack[1:]
    else:
        return Rack[:(ind(letter, Rack))] + Rack[(ind(letter, Rack)+1):]
    
#listOfWords gives us possible words from the defined Dictionary
def listOfWords(Dict, Rack):
    return filter(lambda word: isPossible(word, Rack), Dict)

#isPossible figures out whether or not a word is able to be made from the Rack
def isPossible (word, Rack):
    if word == "":
        return True
    elif word[0] in Rack:
        return isPossible(word[1:], remove(word[0], Rack))
    else:
        return False

   
    
