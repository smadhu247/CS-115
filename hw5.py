'''
Created on 10/11/19
@author:   Sanjana Madhu, collaborator: Michael Gajdosik
Pledge:    I pledge my honor that I have abided by the Stevens Honor System


CS115 - Hw 5
'''

from cs115 import  map, reduce 

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def numToBinary(n):
#converts a base 10 number to binary
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else: 
        return numToBinary(n//2) + '0'
    
def binaryToNum(s):
#converts a binary number to base 10
    if s == "":
        return 0
    else:
        return int(s[-1]) + (2* binaryToNum(s[:-1]))
    
def isOdd(n):
#checks whther the number is even or odd. Used to convert from base 10 to binary
    return n % 2 == 1

def counter(S,C):
#creates a list of elements that shows how many ones and zeros are in the given list of binary numbers. For example, if the list was 00100, the list [2,1,2] will be created
    if len(S) == 1:
        return [C]
    elif S[0]==S[1]:
        return counter(S[1:], C + 1)
    else:
        return [C] + counter(S[1:], 1)


def padZeros(L):
#adds zeros to the front of the sequence if necessary. Also slices if the binary representation exceeds 31.
    if L == []:
        return []
    elif len(str(L[0])) == COMPRESSED_BLOCK_SIZE:
        return [L[0]] + padZeros(L[1:])
    elif len(str(L[0])) < COMPRESSED_BLOCK_SIZE:
        return ["0" * (COMPRESSED_BLOCK_SIZE - len(str(L[0]))) + str(L[0]) ] + padZeros(L[1:])
    elif len(str(L[0])) > COMPRESSED_BLOCK_SIZE:
        remainder = numToBinary(binaryToNum(str(L[0])) - MAX_RUN_LENGTH)
        return ["1111100000"] + padZeros([remainder]) + padZeros(L[1:])
    
def compress(S):
#turns a given binary string into a compressed form through run-length encoding
    initial = counter(S, 1)
    sequence = map(numToBinary, initial)
    digits = padZeros(sequence)
    if S[0] == "1":
        return "00000" + reduce(lambda x, y: x+y, digits)
    else:
        return reduce(lambda x, y: x+y, digits)

def Slice(S):
#slices the String into components of 5 to be used in uncompress
    if S == "":
        return []
    else:
        return [S[0:COMPRESSED_BLOCK_SIZE]] + Slice(S[COMPRESSED_BLOCK_SIZE:])

def uncompress(S):
#reverses the work done by compress. Uses run-length encoded code to turn the sequence back into a regular binary string
    if Slice(S) == []:
        return ""
    else:
        slicedList = Slice(S)
        if len(slicedList) == 1:
            return "0" * binaryToNum(slicedList[0])
        else:
            return "0" * binaryToNum(slicedList[0]) + "1" * binaryToNum(slicedList[1]) + uncompress(S[2 * COMPRESSED_BLOCK_SIZE:])
   
def compression(S):
#return the ratio of the compressed size to the original size for image S.
    return len(compress(S)) / len (S)


"""
1. The largest number of bits that that the compress algorithm could use to encode a 64-bit string or image
is 320 bits because each element would have 5 components.

2. The test I conducted checked if the binary numbers from the picture produce the correct compression if
they're compressed. I created a variable with the image's name (penguin, smile, and five) and set it equal
to its respective binary code. Then I set a variable called sequence equal to the image name. Finally, I used
a self-assert thing to test is compression of the sequence actually produces what is supposed to be produced.

3. A compress algorithm can't always make an output shorter. There is no possible way to compress a bit string
that follows what Prof Lai is saying because the compression isn't necessarily looking to make the binary
sequence shorter. Rather, it is looking to represent it in a different way. Even if Lai tries to represent
the binsary string in bits of 5 in the pattern on 1010101... rather than 010101.... (like we did in the lab),
she will still be unable to make the output shorter. 
"""
