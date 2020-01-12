'''
Author: Sanjana Madhu
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Date: 10/28/19
'''

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + (2* binaryToNum(s[:-1]))
    
def baseBToNum(S, B):
    """converts a base to a different number"""
    if S == "":
        return 0
    else:
        return int(S[-1]) + (B * baseBToNum(S[:-1], B))
    
def numToBaseB(N, B):
    """converts a number to a different base"""
    if N == 0:
        return "0"
    def numToBaseB_helper(N, B):
        if N == 0:
            return ""
    return str(int(numToBaseB(N // B, B) + str(N%B)))
    
def add(S, T):
    """adds two binary numbers by converting them to decimal"""
    S1 = baseBToNum(S, 2)
    T1 = baseBToNum(T, 2)
    binarySum = S1 + T1
    return numToBaseB(binarySum, 2)

def helperTc(s):
    """"flips the bits for 2s complement"""
    if s == "":
        return ""
    elif s[0] == "1":
        return "0" + helperTc(s[1:]) 
    elif s[0] == "0":
        return "1" + helperTc(s[1:]) 

def TcToNum(s):
    """performs 2s complement on a given string of numbers and outputs in decimal form"""
    if s[0] == "0":
        return binaryToNum(s)
    else:
        num = add(helperTc(s), "1")
        return -1 * binaryToNum(num)

def NumToTc(N):
    """performs 2s complement on a given a number in deciaml form and outputs a binary number"""
    if N > 127 or N < -128:
        return "Error"
    if N < 0:
        num = numToBaseB((N * -1),2) 
        if len(num) == 8:
            number = "" + num
        else:
            number = ("0" * (8 - len(num)))  + num
        return add(helperTc(number), "1")
    else:
        num = numToBaseB(N, 2)
        if len(num) == 8:
            return ""
        elif len(num) < 8:
            return ("0" * (8 - len(num)))  + num
        return num

    
