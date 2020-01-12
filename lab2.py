#Sanjana Madhu
#smadhu
#I pledge my honor that I have abided by the Stevens Honor System
def dot(L, K):
    if (L== [] or K == []):
        return 0.0
    elif (len(L) != len(K)):
        if(len(L) > len(K)):
            return len(K) * (L[0]*K[0] + dot(L[1:],K[1:]))
        elif(len(L) < len(K)):
            return len(L) * (L[0]*K[0] + dot(L[1:],K[1:]))
    else: 
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    if (S == ""):
       return [ ]
    else:
       return [(S[0])] + explode(S[1:])

def ind(e, L):
    if not L:
        return len(L)
    elif e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:]) 

def removeAll(e, L):
    if not L:
        return L
    elif e == L[0]:
        return L[1:]
    else:
        return L[:(ind(e, L))] + removeAll(e, L[(ind(e, L)+1):])

def even(X):
    if (X % 2 == 0):
        return True
    else:
        return False
def myFilter(x, L):
    if not L:
        return [ ]
    if x(L[0]) == True:
        return [L[0]] + myFilter(x, L[1:])
    else:
        return myFilter(x, L[1:])
            
def deepReverse(L):
    if L == []:
        return L
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
    
    


