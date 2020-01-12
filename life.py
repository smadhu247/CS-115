#
# life.py - Game of Life lab
#
# Name: Sanjana Madhu
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(0, height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write) """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or col == 0 or row == h-1 or col == w-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w,h):
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or col == 0 or row == h-1 or col == w-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice( [0,1] )
    return A

def copy(A):
    width = len(A[0])
    height = len(A)
    newA = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == 0 or col == 0 or row == (len(A))-1 or col == (len(A[0]))-1:
                A[row][col] = 0
            else:
                if A[row][col] == 0:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
    return A

def countNeighbors(row, col, A):
    n = 0
    for x in range(row - 1, row + 2):
        for y in range(col - 1, col + 2):
            if x != row or y != col:
                if A[x][y] == 1:
                    n = n + 1
    return n

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
"""
    newA = createBoard(len(A), len(A[0]))
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            n = countNeighbors(row, col, A)
            if n < 2 or n > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and n == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA


    

    
