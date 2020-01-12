'''
Created on Mar 1, 2015
Last modified on Mar 4, 2016

@author: Brian Borowski

CS115 - Hw 5 Test Script
'''
import unittest
import hw5

class Test(unittest.TestCase):

    def test01(self):
        sequence = '0' * 64
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '1111100000111110000000010') #31 + 0 + 31 + 0 + 2 = 64
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 0.390625, 4)

    def test02(self):
        sequence = '01' * 32
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 5.0, 4)

    def test03(self):
        sequence = '10' * 32
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 5.078125, 4)

    def test04(self):
        sequence = '0' * hw5.MAX_RUN_LENGTH + '1' * hw5.MAX_RUN_LENGTH + '0' * (64 - 2 * hw5.MAX_RUN_LENGTH)
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '111111111100010')
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 0.234375, 4)

    def test05(self):
        sequence = '0' * (hw5.MAX_RUN_LENGTH + 1) + '1' * (hw5.MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * hw5.MAX_RUN_LENGTH - 2)
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '111110000000001111110000000001')
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 0.46875, 4)

    def test06(self):
        sequence = '1' * hw5.MAX_RUN_LENGTH + '0' * hw5.MAX_RUN_LENGTH + '1' * (64 - 2 * hw5.MAX_RUN_LENGTH)
        compress = hw5.compress(sequence)
        self.assertEqual(compress, '00000111111111100010')
        uncompress = hw5.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw5.compression(sequence), 0.3125, 4)

    def test07(self):
        penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
        sequence = penguin
        self.assertAlmostEqual(hw5.compression(sequence), 1.484375, 4)

    def test08(self):
        smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
        sequence = smile
        self.assertAlmostEqual(hw5.compression(sequence), 1.328125, 4)

    def test09(self):
        five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
        sequence = five
        self.assertAlmostEqual(hw5.compression(sequence), 1.015625, 4)

if __name__ == "__main__":
    unittest.main()
