'''
Name: Sanjana Madhu
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Date: 10/22/19
'''

def numToBaseB(N, B):
    """converts a number to a different base"""
    if N == 0:
        return "0"
    def numToBaseB_helper(N, B):
        if N == 0:
            return ""
    return str(int(numToBaseB(N // B, B) + str(N%B)))


def baseBToNum(S, B):
    """converts a base to a different number"""
    if S == "":
        return 0
    else:
        return int(S[-1]) + (B * baseBToNum(S[:-1], B))

def baseToBase(B1,B2,SinB1):
    """converts between bases"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S, T):
    """adds two binary numbers by converting them to decimal"""
    S1 = baseBToNum(S, 2)
    T1 = baseBToNum(T, 2)
    binarySum = S1 + T1
    return numToBaseB(binarySum, 2)
        
    
# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder ={ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }


def addB(s1, s2):
    """adds two binary numbers by keeping them in binary"""
    return addB_helper(s1, s2, "0")

def addB_helper(s1, s2, carry):
    """helper function to add binary numbers"""
    if s1 == "" and s2 == "":
        if carry == "1":
            return carry
        else:
            return ""
    if s1 == "":
        return addB_helper("0", s2, carry)
    if s2 == "":
        return addB_helper(s1, "0", carry)
    else:
        return addB_helper(s1[:-1], s2[:-1], FullAdder[s1[-1], s2[-1], carry][1]) + FullAdder[s1[-1], s2[-1], carry][0] 
    
    
