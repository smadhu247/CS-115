'''
Created on November 14th, 2019

@author: Sanjana Madhu

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''


import math

class QuadraticEquation():
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient \'a\' cannot be 0 in a quadratic equation.")
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)
      
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def discriminant(self):
        return (self.__b**2) - 4 * self.__a * self.__c

    def root1(self):
        dis = self.discriminant()
        if dis < 0:
            return None
        else:
            return ((-1 * self.__b) + (math.sqrt(dis))) / (2 * self.__a)

    def root2(self):
        dis = self.discriminant()
        if dis < 0:
            return None
        else:
            return ((-1 * self.__b) - (math.sqrt(dis))) / (2 * self.__a)

    def __str__(self):
        if self.__a < 0:
            A = '-'
        else:
            A = ''

        if self.__b < 0:
            B = '-'
        else:
            B = '+'
        
        if self.__c < 0:
            C = '-'
        else:
            C = '+'
            
        if self.__a == 1 or self.__a == -1:
            a = '' + 'x^2 '
        else:
            a = str(abs(self.__a)) + 'x^2 '
            
            
        if self.__b == 0:
            b = '' 
        elif self.__b == 1 or self.__b == -1:
            b = B + ' x '
        else:
            b = B + ' ' + str(abs(self.__b)) + 'x '
            
        if self.__c == 0:
            c = ''
        else:
            c = C + ' ' + str(abs(self.__c)) + ' '
        return A + a + b + c + '= 0'
  
    
    
