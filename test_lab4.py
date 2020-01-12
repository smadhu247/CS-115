'''
Created on September 25, 2019

@author: Charles Fee

CS115 - Lab 4 (Coin Row) Test Script
'''

import unittest
import lab4

class Test(unittest.TestCase):

    def testCoinRow(self):
        self.assertEqual(lab4.coin_row([]), 0)

    def testCoinRow1(self):
        self.assertEqual(lab4.coin_row([5,1,2,10,6,2]), 17)

    def testCoinRow2(self):
        self.assertEqual(lab4.coin_row([10,5,5,5,10,50,1,10,1,1,25]), 100)

    def testCoinRow3(self):
        self.assertEqual(lab4.coin_row([10,3000,40,7,6,2,100]), 3107)

    def testCoinRow4(self):
        self.assertEqual(lab4.coin_row([100000, 999, 405, 39455, 5969, 2345, 1]), 141800)

    def testCoinRowVal(self):
        self.assertEqual(lab4.coin_row_with_values([]), [0, []])

    def testCoinRowVal1(self):
        self.assertEqual(lab4.coin_row_with_values([5,1,2,10,6,2]), [17, [5,10,2]])

    def testCoinRowVal2(self):
        self.assertEqual(lab4.coin_row_with_values([10,5,5,5,10,50,1,10,1,1,25]), [100, [10,5,50,10,25]])

    def testCoinRowVal3(self):
        self.assertEqual(lab4.coin_row_with_values([10,3000,40,7,6,2,100]), [3107, [3000,7,100]])

    def testCoinRowVal4(self):
        self.assertEqual(lab4.coin_row_with_values([100000, 999, 405, 39455, 5969, 2345, 1]), [141800, [100000, 39455, 2345]])


        

if __name__ == "__main__":
    unittest.main()
