'''Created on 9/21/19
@author: Sanjana Madhu
Pledge: I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here


'''this program inputs an amount of money and a list of coins. The program outputs a list containing
the least number of coins used to make the amount and the values of the coins which are in a list
themselves'''
def giveChange(amount, coins):
    if (amount == 0):
        return [0,[]] 
    if (coins == [] or amount < 0):  
        return [float('inf'),[]]
    else:
        if(coins[0]> amount):
            return giveChange(amount, coins[1:])
        else:
            useIt = giveChange(amount - coins[0], coins) 
            loseIt = giveChange(amount, coins[1:])
            if (useIt[0] >= loseIt[0]):
                return loseIt
            else:
                return [1 + useIt[0], useIt[1]+[coins[0]]]
