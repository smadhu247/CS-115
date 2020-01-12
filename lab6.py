'''
Created on 10/9/19
@author:   Sanjana Madhu
Pledge:   I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    #42 in base 2 is 101010
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    #1: if the number given is an odd base-10 number, then the least significant bit will be 1
    #2: if the number given is an even base-10 number, then the least significant bit will be 0
    #3: if we remove the least significant bit, we get the original number // 2 (integer division by 2)
    #4: if we already had the base-2 representation of Y, just add a 1 to the end if N is odd and a 0 if N is positive
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else: 
        return numToBinary(n//2) + '0'
        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + (2* binaryToNum(s[:-1]))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    n = numToBinary(binaryToNum(s) + 1)
    if (s == '11111111'):
       return ('0'*8)
    if (len(n) < 8):
        return ("0" * (8-len(n))) + n
    elif (len(n) > 8):
        return s[-8:]
    else:
        return n

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n > 0:
        count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    #59 in base 3 2012
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + (3 * ternaryToNum(s[:-1]))
