'''Created on 9/25/19
author: Sanjana Madhu
pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

#returns the maximum value the coinrow can make without using values that are adjacent to each other

def coin_row(L):
    if L == []:
        return 0
    else:
        useIt = coin_row(L[2:]) + L[0]
        loseIt = coin_row(L[1:])
        return max(useIt, loseIt)
        
#returns the same as coin_row along with the coins used to create the maximum value

def coin_row_with_values(L):
    if L == []:
        return [0,[]]
    useIt = coin_row_with_values(L[2:])
    useIt[0] += L[0]
    useIt[1] = [L[0]] + useIt[1]
    loseIt = coin_row_with_values(L[1:])
    if (useIt[0] >= loseIt[0]):
        return useIt
    else:
        return loseIt
    
print(coin_row([]))
print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
