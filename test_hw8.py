'''
Created on Apr 1, 2015


@author: Brian Borowski

CS115 - Hw 8 Test Script
'''
import unittest
import hw8

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(hw8.questifyAlt([]), [])
        self.assertEqual(hw8.questifyAlt(['yeah']), ['yeah?'])
        self.assertEqual(hw8.questifyAlt(['yeah', 'really', 'no way']), ['yeah?', 'really?', 'no way?'])

    def test02(self):
        self.assertEqual(hw8.catenateLoop([]), '')
        self.assertEqual(hw8.catenateLoop(['this']), 'this')
        self.assertEqual(hw8.catenateLoop(['this', 'function', 'actually', 'works']), 'thisfunctionactuallyworks')

    def test03(self):
        self.assertEqual(hw8.letterScoreLoop('a', hw8.scrabbleScores), 1)
        self.assertEqual(hw8.letterScoreLoop('f', hw8.scrabbleScores), 4)
        self.assertEqual(hw8.letterScoreLoop('q', hw8.scrabbleScores), 10)
        self.assertEqual(hw8.letterScoreLoop('z', hw8.scrabbleScores), 10)

    def test04(self):
        self.assertEqual(hw8.wordScoreLoop('', hw8.scrabbleScores), 0)
        self.assertEqual(hw8.wordScoreLoop('test', hw8.scrabbleScores), 4)
        self.assertEqual(hw8.wordScoreLoop('zebra', hw8.scrabbleScores), 16)
        self.assertEqual(hw8.wordScoreLoop('manufacturing', hw8.scrabbleScores), 21)

    def test05(self):
        self.assertEqual(hw8.wordsWithScoreLambda([], hw8.scrabbleScores), [])
        self.assertEqual(hw8.wordsWithScoreLambda(['a'], hw8.scrabbleScores), [['a', 1]])
        self.assertEqual(hw8.wordsWithScoreLambda(['python', 'is', 'awesome'], hw8.scrabbleScores), [['python', 14], ['is', 2], ['awesome', 12]])
        self.assertEqual(hw8.wordsWithScoreLambda(hw8.aDictionary, hw8.scrabbleScores), [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]])

    def test06(self):
        self.assertEqual(hw8.wordsWithScoreLoop([], hw8.scrabbleScores), [])
        self.assertEqual(hw8.wordsWithScoreLoop(['a'], hw8.scrabbleScores), [['a', 1]])
        self.assertEqual(hw8.wordsWithScoreLoop(['python', 'is', 'awesome'], hw8.scrabbleScores), [['python', 14], ['is', 2], ['awesome', 12]])
        self.assertEqual(hw8.wordsWithScoreLoop(hw8.aDictionary, hw8.scrabbleScores), [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]])

if __name__ == "__main__":
    unittest.main()
