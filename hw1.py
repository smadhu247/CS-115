#Sanjana Madhu
#smadhu
#I pledge my honor that I have abided by the Stevens Honor System


from cs115 import map, reduce
import math


#task 1
def mult(x, y):
    return x * y

def factorialA(n):
    return reduce(mult, range(1, n+1))

def factorialB(n):
    if (n > 0):
        return n * factorialB(n-1)
    else:
        return 1
    
#task 2
def add(x, y):
    return x + y
def mean(L):
    avg = reduce(add, L)
    return avg/ (len(L))



#task 3
def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    if (n == 1):
        return False
    else:
        return sum(map(divides(n), range(1, int(math.sqrt(n)) + 1)), 0) == 1


