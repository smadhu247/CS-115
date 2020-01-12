'''
Created on 10/3/19
@author: Sanjana Madhu
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

#draws out one side of a snowflake three times 
def snowflakeSide(trunk_length, levels):
    if levels == 0:
        turtle.forward(trunk_length)
        return
    else:
        turtle.pencolor("blue")
        turtle.fillcolor("purple")
        turtle.speed("fastest")
        turtle.filling()
        snowflakeSide(trunk_length/3, levels - 1)
        turtle.left(60)
        snowflakeSide(trunk_length/3, levels - 1)
        turtle.right(120)
        snowflakeSide(trunk_length/3, levels - 1)
        turtle.left(60)
        snowflakeSide(trunk_length/3, levels - 1)

#non-recursive function that calls snowflakeSide 3 times to complete snowflake
def snowflake(trunk_length, levels):
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount,coins)]
        if amount == 0:
            result = 0
        elif len(coins) == 0 or amount < 0:
            result = float("inf")
        else:
            useIt = 1 + fast_change_helper(amount - coins[0], coins, memo)
            loseIt = fast_change_helper(amount, coins[1:], memo)
            result = min(useIt,loseIt)
        memo[(amount, coins)] = result
        return result
    #Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})
    
# If you did this correctly, the results should be nearly instantaneous.
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


# Should take a few seconds to draw a snow flake
snowflake(800, 3)
