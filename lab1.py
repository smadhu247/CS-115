#I pledge my honor that I have abided by the Stevens Honor System
#Sanjana Madhu

from cs115 import map, reduce
import math

#task 1:
def inverse(n):
    return 1/n
print (inverse(3))

#task 2:
def add(x,y):
    return x+y
def e(n):
    #factorial = inverse(math.factorial(n))
    def factorial(n):
        return inverse(math.factorial(n))
    return reduce(add, map(factorial, range(0, n+1)))

#task 3:
def error(n):
    return abs(math.e - e(n))
    
