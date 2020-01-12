#Sanjana Madhu
#smadhu
#I pledge my honor that I have abided by the Stevens Honor System

def change(amount, coins):
    if (amount == 0):
        return 0 
    if (coins == [] or amount < 0):  
        return float('inf')
    else:
        useIt = change(amount - coins[0], coins) + 1
        loseIt = change(amount, coins[1:])
    return min(useIt, loseIt)


